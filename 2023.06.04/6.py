ticket = input('Введите номер из шести цифр: ')

if (int(ticket[0]) + int(ticket[1]) + int(ticket[2])) == (int(ticket[3]) + int(ticket[4]) + int(ticket[5])):
    print("да")
else:
    print("нет")

# Введите номер из шести цифр: 123456
# нет

# Введите номер из шести цифр: 274625
# да