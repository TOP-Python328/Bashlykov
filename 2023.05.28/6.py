square_1 = input('')
square_2 = input('')

# УДАЛИТЬ: условия избыточны
if square_1[0] == square_2[0] and -1 <= int(square_1[1]) - int(square_2[1]) <= 1:
    print('да')
# УДАЛИТЬ: условия избыточны
elif square_1[1] == square_2[1] and -1 <= ord(square_1[0]) - ord(square_2[0]) <= 1:
    print('да')
# КОММЕНТАРИЙ: вот этих проверок достаточно
elif -1 <= ord(square_1[0]) - ord(square_2[0]) <= 1 and -1 <= int(square_1[1]) - int(square_2[1]) <= 1:
    print('да')
else:
    print('нет')


# a4
# a5
# да

# d3
# e4
# да

# f6
# a1
# нет


# ИТОГ: хорошо — 3/4
