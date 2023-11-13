class Point:

    """Описываeт двумерную точку"""

    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y        
    
    def __eq__(self, other): 
        return self.x == other.x and self.y == other.y 
      
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f'({self.x},{self.y})'
    
    @property
    def x(self) -> float:
        return self.__x
    
    @x.setter
    def x(self, value) -> 'TypeError':
        raise TypeError("'Point' object does not support coordinate assignment")
        
    @property
    def y(self) -> float:
        return self.__y
    
    @y.setter
    def y(self, value) -> 'TypeError':
        raise TypeError("'Point' object does not support coordinate assignment")


class Line:

    """Описываeт отрезок"""
  
    def __init__(self, start: Point, end: Point):
        self.__start = start
        self.__end = end
        self.__length: float = self.length_calc(start, end) 
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f'{self.start}———{self.end}'
        
    @staticmethod
    def length_calc(point1: Point, point2: Point) -> float:
    
        """Вычисляет расстояние между двумя точками"""
        
        return ((point2.x - point1.x)**2 + (point2.y - point1.y)**2) ** 0.5
   
    @property
    def start(self) -> Point:
        return self.__start
        
    @start.setter
    def start(self, new_point: Point) -> None:
        if isinstance(new_point, Point):
            self.__start = new_point
            self.__length = self.length_calc(self.start, self.end) 
        else:
            raise TypeError("'start' attribute of 'Line' object supports only 'Point' object assignment")
            
    @property
    def end(self) -> Point:
        return self.__end
        
    @end.setter
    def end(self, new_point: Point) -> None:
        if isinstance(new_point, Point):
            self.__end = new_point
            self.__length = self.length_calc(self.start, self.end) 
        else:
            raise TypeError("'end' attribute of 'Line' object supports only 'Point' object assignment")
            
    @property
    def length(self) -> float:
        return self.__length
        
    @length.setter
    def length(self, value) -> 'TypeError':
        raise TypeError("Line' object does not support length assignment")
       
   
class Polygon(list):

    """Описываeт многоугольник"""
    
    def __init__(self, side1: Line, side2: Line, side3: Line, *sides: Line):
        super().__init__([side1, side2, side3, *sides])
    
    def is_closed(self) -> bool:
    
        """Проверяет, формируют ли отрезки замкнутый многоугольник"""
        
        if self[0].start != self[-1].end:
            return False
        return all(self[i].end == self[i + 1].start for i in range(len(self) - 1))    
    
    @property
    def perimeter(self) -> float:
    
        """Вычисляет периметр многоугольника"""
        
        if self.is_closed():
            return sum(line.length for line in self)
        else:
            raise ValueError("line items doesn't form a closed polygon")
            
            
# >>> p1 = Point(0,0)
# >>> p2 = Point(2,2)
# >>> p3 = Point(0,3)
# >>> p1
# (0,0)
# >>> repr(p1) == str(p1)
# True
# >>> repr(p1) == str(p2)
# False
# >>> p1 == p2
# False
# >>> p2 == Point(2,2)
# True
# >>> p1.x, p1.y
# (0, 0)
# >>> p1.x = 5
#... TypeError: 'Point' object does not support coordinate assignment
# >>> p1.y = 5
# ...TypeError: 'Point' object does not support coordinate assignment
# >>> l1 = Line(p1, p2)
# >>> l2 = Line(p2, p3)
# >>> l3 = Line(p3, p1)
# >>> l1
# (0,0)———(2,2)
# >>> repr(l1) == str(l1)
# True
# >>> l1.length
# 2.8284271247461903
# >>> l1.length = 10
# ...TypeError: Line' object does not support length assignment
# >>> l1.start = 10
# ...TypeError: 'start' attribute of 'Line' object supports only 'Point' object assignment
# >>> l1.end = 10
# ... TypeError: 'end' attribute of 'Line' object supports only 'Point' object assignment
# >>> pol1 = Polygon(l1, l2, l3)
# >>> pol1.perimeter
# 8.06449510224598
# >>> pol1.perimeter = 20
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# ...AttributeError: property 'perimeter' of 'Polygon' object has no setter
# >>> l3.end = Point(10,10)
# >>> pol1[-1]=l3
# >>> pol1.perimeter
# ...ValueError: line items doesn't form a closed polygon
# >>>