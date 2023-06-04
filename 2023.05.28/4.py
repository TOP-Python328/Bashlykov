square_1 = input('')
square_2 = input('')
black_square = ('a1 a3 a5 a7 b2 b4 b6 b8 c1 c3 c5 c7 d2 d4 d6 d8 e1 e3 e5 e7 f2 f4 f6 f8 g1 g3 g5 g7 h2 h4 h6 h8')

black_squares = black_square.split()
if square_1 in black_squares and square_2 in black_squares:
    print("да")
elif square_1 not in black_squares and square_2 not in black_squares:
    print("да")
else:
    print("нет")
    
# c4
# f8
# нет

# d2
# g5
# да