fruits_list = []
while True:
    fruit = input('введите фрукт: ')
    if fruit == '':
        break
    else:
        fruits_list += [fruit]
if len(fruits_list) == 1:
        print(fruits_list[0])
else:
    print(', '.join(fruits_list[:-1]), f'и', ''.join(fruits_list[-1:]))

# введите фрукт: банан
# введите фрукт: слива
# введите фрукт: киви
# введите фрукт: манго
# введите фрукт:
# банан, слива, киви и манго