number_1 = int(input(''))
number_2 = int(input(''))

if number_1 % number_2 == 0:
    print(f'{number_1} делится на {number_2} нацело\n'
          f'частное: {number_1 // number_2}')
elif number_1 % number_2 > 0:
    print(f'{number_1} не делится на {number_2} нацело\n'
          f'неполное частное: {number_1 // number_2}\n'
          f'остаток: {number_1 % number_2}')
# 5
# 2
# 5 не делится на 2 нацело
# неполное частное: 2
# остаток: 1

# 45
# 9
# 45 делится на 9 нацело
# частное: 5