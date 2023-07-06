def math_function_resolver(math_func: 'callable', *numbers: tuple[float | int], switch: bool=False) -> list[float | str]:
    """ Функция вычисляет округлённые значения для различных математических функций.
     Параметры:
        math_func: Вызываемый объект. Ожидает один обязательный аргумент.
        numbers: Кортеж объектов int или float, передаваемых в вызываемый объект.
        switch: Строго ключевой параметр, передаётся в виде объекта bool, значение по умолчанию False. Возвращает строковое представление результатов вычисления если передано значение True 
    Возвращаемое значение:
        Объект списка с вычисленными значениями математической функции для переданных значений x.
    """
    result = []
    
    for num in numbers:
        result.append(round(math_func(num),1))
            
    return [str(num) for num in result] if switch else result
    
# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10), switch=True)
# ['2.5', '3.0', '3.5', '4.0', '4.5', '5.0', '5.5', '6.0', '6.5']
# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]
# >>> math_function_resolver(lambda x: 1*x + 2, *range(1, 10), switch=True)
# ['3', '4', '5', '6', '7', '8', '9', '10', '11']
