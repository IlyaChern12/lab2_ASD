from math import *

graph = [[0, 5, inf, inf],
         [50, 0, 15, 5],
         [30, inf, 0, 15],
         [15, inf, 5, 0]]
n = len(graph)
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in graph:
    print(row)
