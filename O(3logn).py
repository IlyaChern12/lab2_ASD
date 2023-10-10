def binary_search(data, elem):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == elem:
            return 1
        elif data[mid] > elem:
            high = mid - 1
        else:
            low = mid + 1

inp_tre = map(int, input('Введите три числа: ').split())
search_arr = map(int, input('Введите массив чисел: ').split())
res = 0
for elem in inp_tre:
    res += binary_search(search_arr, elem)
print(f'Найдено элементов: {res}') 
