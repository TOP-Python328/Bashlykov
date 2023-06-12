num_digit = int(input('Введите количество разрядов: '))
max_num = int(num_digit * '9')
count_numbers = 0

for num in range((max_num + 1) // 10, max_num + 1):
    for x in range(2, num):
        if num % x == 0:
            break
    else:
        count_numbers += 1
print(count_numbers)
    
# Введите количество разрядов: 3
# 143

# Введите количество разрядов: 5
<<<<<<< HEAD
# 8363
=======
# 8363
>>>>>>> 76f9e3ca053917373011984dee994dc9c16f274e
