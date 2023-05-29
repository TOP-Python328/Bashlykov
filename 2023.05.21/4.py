# ПЕРЕИМЕНОВАТЬ: число — number, num
a = int(input(' '))
# ПЕРЕИМЕНОВАТЬ: цифра числа — digit
c = a // 100
d = (a % 100) // 10
e = (a % 100) % 10

print(f'Сумма цифр = {c + d + e}\n'
      f'Произведение цифр = {c * d * e}')

#  753
# Сумма цифр = 15
# Произведение цифр = 105

# ИТОГ: очень хорошо — 4/4

# ИСПРАВЛЕНИЯ:

number = int(input(''))

digit_1 = number // 100
digit_2 = (number % 100) // 10
digit_3 = (number % 100) % 10

print(f'Сумма цифр = {digit_1 + digit_2 + digit_3}\n'
      f'Произведение цифр = {digit_1 * digit_2 * digit_3}')
      
