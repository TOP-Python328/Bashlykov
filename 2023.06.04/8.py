num_list = [1]
num_fib1 = 1
num_fib2 = 1

number = int(input('требуемое количество чисел последовательности Фибоначчи: '))
if number == 1:
    print(num_fib1)
elif number == 2:
    print(num_fib1,num_fib2 )
else:
    for i in range(number-2):
        n = num_list[i] + num_list[i-1]
        num_list += [n]
    print(num_fib2, *num_list)

# требуемое количество чисел последовательности Фибоначчи: 2
# 1 1

# требуемое количество чисел последовательности Фибоначчи: 19
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181


