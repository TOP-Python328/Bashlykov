# ПЕРЕИМЕНОВАТЬ: sum — это имя встроенной функции, объявляя собственную переменную с таким именем вы теряете прямой доступ к встроенной функции, лучше использовать sum_ или numbers_sum
sum = 0

number_1 = float(input(''))
number_2 = float(input(''))
number_3 = float(input(''))

if number_1 > 0:
    sum += number_1
if number_2 > 0:
    sum += number_2
if number_3 > 0:
    sum += number_3

print(sum)


# 1.5
# -6.3
# 6
# 7.5


