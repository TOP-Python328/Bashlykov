from datetime import datetime as dt
    
def logger(function: 'callable') -> 'callable':

    """Фукнкция декоратор, который в стандартном потоке вывода ведёт журнал вызовов декорируемой функции"""
          
    def wrapper(*args, **kwargs) -> 'any':
    
        now = dt.now()
        today = now.strftime('%Y.%m.%d %H:%M:%S')
        
        arguments =[f'{arg}' for arg in args] + [f'{k}={v}' for k, v in kwargs.items()] 
                
        if function.__defaults__ is not None:
            for def_arg in function.__defaults__:
                if function.__code__.co_argcount != len(args):
                    arguments += [f'{def_arg}']                    
               
        if function.__kwdefaults__ is not None:
            for k, v in function.__kwdefaults__.items():
                if k not in kwargs:
                    arguments += [f'{k}={v}']
        
        print_log = f'{today} - {function.__name__}({", ".join(arguments)}) -> '
        
        with open('data\\function_calls.log', mode = 'a', encoding = 'utf-8') as filein:
            filein.write(print_log)
             
            try: 
                result = function(*args, **kwargs)
                filein.write(f'{result}\n')
                return result
            except Exception as exception:
                log_exception = f'{type(exception).__name__}: {str(exception)}'
                print(f'\t{log_exception}')
                filein.write(f'{log_exception}\n')             
          
    return wrapper
    
# C:\Users\Asus\OneDrive\Рабочий стол\Program\dz_python\Bashlykov\2023.07.02
 # 22:10:45 > python -i 5.py
# >>> def testing_function():
# ...     pass
# ...
# >>> testing_function = logger(testing_function)
# >>> testing_function()
# >>> def div_round(num1, num2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>> div_round(2, 3, digits=4)
# 0.6667
# >>> div_round(2, 0, digits=4)
        # ZeroDivisionError: division by zero
# >>>

# 2023.06.09 09:17:51 - testing_function() -> None
# 2023.06.09 09:18:26 - div_round(2, 3, digits=4) -> 0.6667
# 2023.06.09 09:18:33 - div_round(2, 0, digits=4) -> ZeroDivisionError: division by zero