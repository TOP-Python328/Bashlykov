def countable_nouns(number: int, words: tuple[str, str, str]) -> str:

    """Вычесляет и возвращает существительное русского языка (строка), согласованное с числом"""
    list_1= [2, 3, 4]
    list_2= [11, 12, 13, 14]
    list_3 = [0, 5, 6, 7, 8, 9]

    if number % 100 in list_2:
        return words[2]
    elif number % 10 in list_1:
        return words[1]
    elif number % 10 in list_3:
        return words[2]
    else:
        return words[0]
        
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(13, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(11, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(54, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(156, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(114, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(121, ("год", "года", "лет"))
# 'год'
# >>>