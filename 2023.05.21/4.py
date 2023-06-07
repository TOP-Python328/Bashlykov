number = int(input(''))

digit_1 = number // 100
digit_2 = (number % 100) // 10
digit_3 = (number % 100) % 10

print(f'Сумма цифр = {digit_1 + digit_2 + digit_3}\n'
      f'Произведение цифр = {digit_1 * digit_2 * digit_3}')


# ИСПРАВИТЬ: уже не так
#  753
# Сумма цифр = 15
# Произведение цифр = 105


# ИТОГ: очень хорошо — 4/4
