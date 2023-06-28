def orth_triangle(*, cathetus1: float = 0, cathetus2: float = 0, hypotenuse: float = 0) -> float | None:
    """Вычисляет третью сторону прямоугольного треугольника по двум переданным """
    
    if hypotenuse == 0:
        return (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5
    if cathetus1 == 0 and cathetus2 < hypotenuse:
        return (hypotenuse ** 2 - cathetus2** 2) ** 0.5
    if cathetus2 == 0 and cathetus1 < hypotenuse:
        return (hypotenuse ** 2 - cathetus1** 2) ** 0.5
    if cathetus1 > hypotenuse or cathetus2 > hypotenuse:
        return print("None")
        
# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=3, hypotenuse=2)
# None
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0