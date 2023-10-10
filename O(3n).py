inp_arr = map(int, input('Введите массив чисел: ').split())
sum = 0
mult = 1
quad_sum = 0
for elem in inp_arr:
    sum += elem
for elem in inp_arr:
    mult *= elem
for elem in inp_arr:
    quad_sum += elem**2
print(sum, mult, quad_sum)
