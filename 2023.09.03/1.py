class Tetrahedron:
    """Класс с методами вычисления площади поверхности и объема тела тетраэдра"""
    def __init__(self, edge: float):
        self.edge = float(edge)

    # УДАЛИТЬ: не было в задании такого метода
    def edge(self) -> float:
        return self.edge
    
    def surface(self) -> float:
        """Вычисляет площадь поверхности"""
        return 3**0.5 * self.edge**2
    
    def volume(self) -> float:
        """Вычисляет объём тела"""
        return self.edge**3 * 2**0.5 / 12


# >>> t1 = Tetrahedron(5)
# >>> t1.edge
# 5.0
# >>> t1.surface()
# 43.30127018922193
# >>> t1.volume()
# 14.73139127471974
# >>> t2 =Tetrahedron(6)
# >>> t2.edge
# 6.0
# >>> t2.surface()
# 62.35382907247958
# >>> t2.volume()
# 25.455844122715714


# ИТОГ: очень хорошо — 3/3
