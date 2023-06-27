def numbers_strip(sample: list[float], n: int = 1, *, copy: bool = False) -> list:
    """Удаляет n минимальных и n максимальных чисел из списка, возвращает исходный объект списка с внесёнными изменениями или его изменённую копию в виде объекта list"""
     
    while n > 0:
        sample.remove(max(sample))
        sample.remove(min(numbers))
        n -= 1 
    if copy:
        return sample.copy()
    else:
        return sample

# >>> sample = [1, 2, 3, 4 ,5 ,6]
# >>> sample_stripped = numbers_strip(sample, 3)
# >>> sample_stripped
# []
# >>> sample is sample_stripped
# True
# >>> sample
# []

# >>> sample = [10, 20, 30, 40, 50, 60, 70]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30, 40, 50]
# >>> sample is sample_stripped
# False
# >>> sample
# [30, 40, 50]