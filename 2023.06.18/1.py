def strong_password(password: str) -> bool:
    """Проверяет надежность пароля условиям и возвращает объект true если пароль надежный, и объект false, если нет"""
    capital_letter = {chr(code) for code in range(65, 91)}
    # capital_letter = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')             не знаю что вычислит быстрее: генерат выражение для функции chr() или перебор множества при пересечении
    lowercase_letter = {chr(code) for code in range(97, 123)}
    # lowercase_letter = set('abcdefghijklmnopqrstuvwxyz')
    numerals = {chr(code) for code in range(48, 58)}
    # numerals = set('1234567890')
    punctuation_marks = set('!\"#$%&\'()*+,-./:;<=>?@[\\]^_`\{\|\}~ ')
    
    if (len(password) >= 8 and
        set(password) & capital_letter and
        set(password) & lowercase_letter and
        set(password) & punctuation_marks and
        len([i for i in password if i in numerals]) >= 2
        ):
        return True
        
    return False
    
