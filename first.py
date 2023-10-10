def bubble_sort(my_list):

    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list

print(bubble_sort(list(map(int, input().split()))))
