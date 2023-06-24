scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

word = input("Введите одно слово: ").upper().replace('Ё', 'Е')
scores_word = 0

for i in word:
    for key, value in scores_letters.items():
        if i in value:
            scores_word += key
print(scores_word)

# Введите одно слово: ёжик
# 9
# Введите одно слово: синхрофазотрон
# 29