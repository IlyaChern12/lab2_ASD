from random import *

matr_sizes = [randint(2, 10) for i in range(int(input('Введите количество матриц: ')) + 1)]
#matr_sizes = [7, 2, 1, 1]

def matrix_minimize(sizes, i, j):
    mi_cost = float('inf')

    if j <= i + 1:
        return (0, 0)

    for k in range(i + 1, j):
        cost = matrix_minimize(sizes, i, k)[0]
 
        cost += matrix_minimize(sizes, k, j)[0]
 
        cost += sizes[i] * sizes[j] * (sizes[k] * 2 - 1)
 
        if cost < mi_cost:
            mi_k = k

        mi_cost = min(cost, mi_cost)
        
    return (mi_cost, mi_k)

ans = matrix_minimize(matr_sizes, 0, len(matr_sizes) - 1)

print(matr_sizes)
for i in range(len(matr_sizes) - 1):
    print(f'Матрица {matr_sizes[i]}x{matr_sizes[i + 1]} ')

print(f'Разбиение по {ans[1]} матрице. Количество скалярных операций: {ans[0]}')