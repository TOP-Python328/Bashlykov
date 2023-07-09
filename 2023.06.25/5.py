def logger(func: 'callable') -> 'callable':
    """Декоратор, который в стандартном потоке вывода ведёт журнал вызовов декорируемой функции"""
    def wrapper(*args, **kwargs):
        call_log = []

        for i in args:
            call_log.append(f'{i}')

        for key, value in kwargs.items():
            call_log.append(f'{key}={value}')

        if func.__defaults__:
            for arg in func.__defaults__:
                call_log.append(f'{arg}')

        if func.__kwdefaults__:
            for key, value in func.__kwdefaults__.items():
                if key not in kwargs:
                    call_log.append(f'{key}={value}')
                    
        print(f'{func.__name__}({", ".join(call_log)}) -> ', end = '')

        try:
            result = func(*args, **kwargs)
            if result:
                print(result)
            else:
                print()
            return result
        except Exception as exception:
            print(f'\n\t {type(exception).__name__}: {str(exception)}')

    return wrapper
    
# >>> def div_round(num1, num2, *, digits=0):
# ...    return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>>
# >>> div_round(1, 3, digits=2)
# div_round(1, 3, digits=2) -> 0.33
# 0.33
# >>> div_round(7, 2)
# div_round(7, 2, digits=0) -> 4.0
# 4.0
# >>> div_round(19, 3, digits=4)
# div_round(19, 3, digits=4) -> 6.3333
# 6.3333
# >>> div_round(5, 0)
# div_round(5, 0, digits=0) ->
         # ZeroDivisionError: division by zero