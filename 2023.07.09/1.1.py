from collections.abc import Iterable

def product(numbers: Iterable[float]) -> float:
    
    """Рекурсивная функция, которая возвращает произведение чисел"""
    if not numbers:
        return None
    elif 0 in numbers:
        return 0.0
    
    result = 1.0
    
    if isinstance(numbers, dict):
        numbers = list(numbers.values())
     
    for elem in numbers:
        if isinstance(elem, Iterable):
            result *= product(elem)
        else:
            result *= elem
    
    return result
  
   

# >>> print(product((0)))
# None
# >>> print(product([0]))
# 0.0
# >>> print(product([]))
# None
# >>> print(product({}))
# None
# >>> product({'a': 23, 'b' : 36, 'c' : [1,2,3]})
# 4968.0
# >>> product([num for num in range(1,6)])
# 120.0
# >>> product((0.12, 0.05, -0.09, 0.0, 0.21))
# 0.0
# >>> product([10,20,10])
# 2000.0
# >>> product({'a': 23, 'b' : 36, 'c' : 0})
# 0.0
# >>> product([10,2,[1.5]])
# 30.0
# >>> product([10,2,[1.5,[10,2]]])
# 600.0
# >>>


    
    
    
# from collections.abc import Iterable

# def product(numbers: Iterable[float]) -> float:
    
    # """Рекурсивная функция, которая возвращает произведение чисел"""

    # if not numbers:
        # return 1.0
        
    # if isinstance(numbers, dict):
        # numbers = list(numbers.values())
    # elif 0 in numbers:
        # return 0.0
    
    # result = numbers[0] * product(numbers[1:])
    
    # return result
    
    # 0!=1 (факториал нуля равен единице). В математике  «произведение» без каких-либо факторов оценивается как 1. 
    # Допущение «произведения» с нулевыми факторами уменьшает количество случаев, которые необходимо учитывать во многих математических формулах. 
    # Такой «продукт» является естественной отправной точкой в ​​индукционных доказательствах, а также в алгоритмах. 
    # По этим причинам соглашение «пустой продукт равен единице» является обычной практикой в ​​математике и компьютерном программировании.
    # Исходя из этого в этом решении рекурсивная функция в случаях когда переданный аргумент пуст возвращает 1.
