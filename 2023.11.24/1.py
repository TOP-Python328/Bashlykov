from typing import Self

class ClassBuilder:
    """Формирует текст кода класса"""

    def __init__(self, class_name: str):
        self.class_name = class_name
        self.field = []
        self.attr = []

    def add_cls_field(self, name: str, value: str | int) -> Self:
        """Добавляет в класс поля класса со значениями"""
        
        field = f'{name} = {repr(value)}'
        self.field.append(field)
        return self
    
    def add_inst_attr(self, name: str, value: str | int) -> Self:
        """Добавляет в конструктор атрибуты экземпляра со значениями"""
        attr = f'self.{name} = {repr(value)}'
        self.attr.append(attr)
        return self
        
    def __str__(self):
        """Возвращает строковое представление объекта ClassBuilder"""
        indent: str = ' ' * 4
        str_repr_field = ''
        str_repr_attr = ''
        if self.field:
            str_repr_field = '\n'.join(f'{indent}{field}' for field in self.field) + '\n\n'
        if self.attr:
            str_repr_attr = '\n'.join(f'{indent*2}{attr}' for attr in self.attr)
        if not self.field and not self.attr:
            return f'class {self.class_name}:\n{indent}pass'
            
        return f'class {self.class_name}:\n'\
               f'{str_repr_field}'\
               f'{indent}def __init__(self):\n'\
               f'{str_repr_attr}'
               
# C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24
 # 17:09:12 > python -i 1.py
# >>> builder = ClassBuilder('Person').add_inst_attr('name', 'Alex').add_inst_attr('age', 45)
# >>> print(builder)
# class Person:
    # def __init__(self):
        # self.name = 'Alex'
        # self.age = 45
# >>> builder = ClassBuilder('Test').add_cls_field('__protected', []).add_inst_attr('foo', 'bar')
# >>> print(builder)
# class Test:
    # __protected = []

    # def __init__(self):
        # self.foo = 'bar'
# >>> builder = ClassBuilder('Person')
# >>> print(builder)
# class Person:
    # pass
# >>>