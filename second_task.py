from collections import *
from queue import *

graph = {
    'A': ['B', 'C', 'D', 'E', 'F'],
    'B': ['A'],
    'C': ['A', 'E'],
    'D': ['A', 'E'],
    'E': ['A', 'C', 'D', 'G'],
    'F': ['A'],
    'G': ['E']
}

def wfind(start, end):
    queue = Queue() # очередь
    queue.put([start])

    while queue:
        road = queue.get()
        high = road[-1]

        if high == end:
            return road

        for neighb in graph[high]:
            if neighb not in road:
                new_road = list(road)
                new_road.append(neighb)
                queue.put(new_road)

    return []

def dfind(start, end): 
    stack = deque() # стек
    stack.append((start, [start]))
    short_road = []

    while stack:
        high, road = stack.pop()

        if high == end:
            if short_road == [] or len(road) < len(short_road):
                short_road = road
            continue

        for child in graph[high]:
            if child not in road:
                new_road = road + [child]
                stack.append((child, new_road))

    return short_road

print(*wfind('C', 'D'), sep = ' -> ')
print(*dfind('C', 'D'), sep = ' -> ')