binary_number = input('Введите двоичное число: ')

if binary_number[:2] in {'b1', 'b0', '0b','01', '10',  '11', '00', '1', '0'}:
    if set(binary_number[2:]) <= {'0', '1'}:
        print("Да")
    else:
        print("нет")
        
# Введите двоичное число: 0b01111
# Да
# Введите двоичное число: 10000000
# Да
# Введите двоичное число: 012354
# нет
# Введите двоичное число: 01b1
# нет

 # оператор in (проверка наличия элемента в множестве), а также оператор <= (метод .issubset() - проверка, является ли одно множество подмножеством другого) взял из интернета. На уроке не брали
 















# print(set(binary_number))
# print(set(binary_number[:2]))
# print(set(binary_number[2:]))
# print(binary_number)
# print(binary_number[:2])
# print(binary_number[2:])
