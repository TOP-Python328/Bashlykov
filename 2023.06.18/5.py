def central_tendency(num1: float, num2: float, / , *numbers: float) -> dict[str, float]:
    """Вычисляет и возвращает словарь с основными мерами центральной тенденции для некоторого количества чисел"""
    numbers = sorted((num1, num2) + numbers)
    length = len(numbers)
    median_index = length // 2
    arithmetic = sum(numbers) / length
    product_of_values = 1
    sum_of_values= 0
    
    if length % 2 == 0:
        median = float((numbers[median_index - 1] + numbers[median_index]) / 2)
    else:
        median = float(numbers[median_index])
    
    for i in numbers:       
        product_of_values *= i 
        sum_of_values += 1 / i
        
    geometric = product_of_values ** (1 / length)
    harmonic = length / sum_of_values
    
    dict_tendency = {
                'median': median,
                'arithmetic': arithmetic,
                'geometric': geometric,
                'harmonic': harmonic
                }
    return dict_tendency
    
# >>> central_tendency(1.2, 2.3, 3.5, 4)
# {'median': 2.9, 'arithmetic': 2.75, 'geometric': 2.4932124071502657, 'harmonic': 2.2175035868005737}
# >>> central_tendency(1.2, 2.3, 3.5, 4.3, 5.2)
# {'median': 3.5, 'arithmetic': 3.3, 'geometric': 2.9301495400966893, 'harmonic': 2.5269166407732824}
# >>> central_tendency(1, 3, 8, 9, 11, 12)
# {'median': 8.5, 'arithmetic': 7.333333333333333, 'geometric': 5.5271927972486115, 'harmonic': 3.4409847936278064}
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}