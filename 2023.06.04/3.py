number = int(input('Введите натуральное число: '))
num_list = [1,number]

for i in range(2,number):
    if number % i == 0:
        num_list += [i]
        num_list += [(number // i)]
        
number_unique = []
for num in num_list:
    if num not in number_unique:
        number_unique += [num]
        
print(sum(number_unique))

# Введите натуральное число: 96
# 252
