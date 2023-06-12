# num_position = int(input('Введите количество разрядов: '))
# max_num = int(num_position * '9')
# count_numbers = 0

# for num in range((max_num + 1) // 10, max_num + 1):
    # div = 2
    # while div * div <= num:
        # if not num % div:
            # break
        # div += 1
    # else: 
        # count_numbers += 1
# print(count_numbers)        

text = input()
punctuation = '.,:;!?–—\'\"()*/'
text_clean = ''.join(char for char in text if char not in punctuation)
print(text_clean)