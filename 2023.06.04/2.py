sum_ = 0
number = int(input('число: '))
while number > 0:
    n = input('введите целое число: ')
    if not n :
        break
    if int(n) > 0:
        sum_ += int(n)
    number -= 1
print(sum_)

# число: 6
# введите целое число: 5
# введите целое число: 14
# введите целое число: -6
# введите целое число: 16
# введите целое число: -123
# введите целое число: 7
# 42
    


