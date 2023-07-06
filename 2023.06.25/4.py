#def repeat(func: 'callable') -> 'callable':
    """Декоратор, который выполняет декорируемую функцию десять раз"""
    def wrapper(*args, **kwargs):
        for i in range(10):
            func(*args, **kwargs)
    return wrapper
    
# >>> def testing_function():
# ...     print('bashlykov')
# ...
# >>> testing_function = repeat(testing_function)
# >>> testing_function()
# bashlykov
# bashlykov
# bashlykov
# bashlykov
# bashlykov
# bashlykov
# bashlykov
# bashlykov
# bashlykov
# bashlykov
# >>>


