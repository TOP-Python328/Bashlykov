from abc import ABC, abstractmethod
from datetime import datetime as dt, date
from decimal import Decimal as dec
from dataclasses import dataclass
from enum import Enum 
from typing import Literal, Self, Any
import data
 
#HUMAN

@dataclass
class Contact:
    """Контактные данные"""
    mobile: str = None
    office: str = None
    email: str = None
    web: str = None
    telegram: str = None
    
class Person(ABC):
    """Ф.И.О и данные человека"""
    
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            birthdate: str,
            contact: Contact = None,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
        self.birthdate = dt.strptime(birthdate, '%d.%m.%Y').date() 
        self.contact = Contact

    def __repr__(self):
        return f'<ФИО:{self.last_name} {self.first_name[0]}.{self.patr_name[0]}. дата рождения: {self.birthdate}>'

class Student(Person):
    """Студент"""
    
    class EducationForm(Enum):
        """Формат обучения"""
        
        INTRAMURAL = 'очная'
        EXTRAMURAL = 'заочная'
        REMOTE = 'удаленная'
        
        def __repr__(self):
            return f'<{self.__dict__["_name_"]}: {self.__dict__["_value_"]}>'
        
    class ContractForm(Enum):
        """Форма договора"""
        
        BUDGET = 'бюджетный'
        COMPANY = 'целевой'
        PERSONAL = 'персональный'
        
        def __repr__(self):
            return f'<{self.__dict__["_name_"]}: {self.__dict__["_value_"]}>'
        
    
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            birthdate,
            id_group: str = '',
            gradebook: Any = None,
            contact: Contact = None,
            id: int = 100001,
            form: Literal['очная', 'заочная', 'удаленная'] = 'очная',
            contract: Literal['бюджетный', 'целевой', 'персональный'] = 'бюджетный',
            semester: int = 1,
            stipendia: dec = 100
    ):
        super().__init__(last_name, first_name, patr_name, birthdate, contact)
        self.id_group = id_group
        self.id = id
        self.form = Student.EducationForm(form)
        self.contract = Student.ContractForm(contract)
        self.semester = semester
        self.gradebook = gradebook
        self._stipendia = stipendia
        
    @property
    def stipendia(self) -> None:
        """геттер"""
        return self._stipendia
        
    @stipendia.setter
    def stipendia(self, new_stipendia: dec) -> None:
        """setter"""
        self._stipendia = new_stipendia
        
    def __repr__(self):
       return f'<ФИО:{self.last_name} {self.first_name[0]}.{self.patr_name[0]}., ID = {self.id}, форма обучения: {self.form.__dict__["_value_"]}>'
       

class Employee(Person, ABC):
    """Работник"""
    
    class Position(Enum):
        """должность"""
        MAINTENANCE_WORKER = 'обслуживающий работник'
        ADMINISTEACHERTRATIVE_WORKER = 'административный работник'
        TEACHER = 'учитель'
        LABORATORY_ASSISTANT = 'лаборант'
        
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            birthdate,
            contact: Contact = None,
            position: Literal['обслуживающий работник', 'административный работник', 'учитель', 'лаборант'] = 'учитель',
            income: dec = 1000,
    ):
        super().__init__(last_name, first_name, patr_name, birthdate, contact)
        self.position = Employee.Position(position)
        self.income = income
    
    @abstractmethod
    def calc_month_income(self) -> dec:
        """Зарплата"""
        pass


class Teacher(Employee):
    """Преподаватель"""
    
    class Degree(Enum):
        """Ученая степень"""
        CANDIDATE = 'кандидат'
        DOCTOR = 'доктор'
    
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            birthdate,
            contact: Contact = None,
            position: Literal['работник по обслуживанию', 'административный работник', 'учитель', 'лаборант'] = 'учитель',
            income: str = 1000, 
            courses: list[str] = [],
            degree: Literal['кандидат', 'доктор'] = 'кандидат',
            professor: bool = False
    ):
        super().__init__(
            last_name, 
            first_name, 
            patr_name, 
            birthdate, 
            contact, 
            position, 
            income
        )
        self.courses = courses
        self.degree = Teacher.Degree(degree)
        self.professor = professor
        
    def calc_month_income(self) -> dec:
        """Расчёт зарплаты с учетом должности, учебных часов и тд"""
        pass
        
        
    def make_examination(self) -> 'GradeRecord':
        """Провести экзамен - поставить отметку в зачетку"""
        pass
        
    def __repr__(self):
           return f'<ФИО:{self.last_name} {self.first_name[0]}.{self.patr_name[0]}. должность: {self.position.__dict__["_value_"]}, ученая степень: {self.degree.__dict__["_value_"]}>'
           
           
class Administrator(Employee):
    """Администратор"""
    
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            birthdate: dt,
            contact: Contact = None,
            position: Literal['обслуживающий работник', 'административный работник', 'учитель', 'лаборант'] = 'административный работник',
            income: str = 900, 
            head: Self = None,
            subordinates: list[Employee] = []
    ):
        super().__init__(
            last_name, 
            first_name, 
            patr_name,
            birthdate, 
            contact,             
            position, 
            income
        )
        self.head = head
        self.subordinates = subordinates
    
    
    def calc_month_income(self) -> dec:
        """Расчёт оплаты труда - оклад + премия"""
        pass


    def __repr__(self):
           return f'<ФИО:{self.last_name} {self.first_name[0]}.{self.patr_name[0]}. дата рождения: {self.birthdate} должность: {self.position.__dict__["_value_"]}, начальник: {self.head}>'
           
           
class GradeRecord():
    """Отметка в зачётной книжке"""
    
    class ExamType(Enum):
        """Тип экзамена"""
        CHECK = 'зачёт'
        DIFF_CHECK = 'диференцированный зачёт'
        EXAMEN = 'экзамен'
        PROJECT = 'проект'
    def __init__(
            self,
            date: str,
            examiner: Teacher,
            semester: int = 1,
            type: Literal['зачёт', 'диференцированный зачёт', 'экзамен', 'проект'] = 'зачёт',
            grade: int = None,
            scale: int = 5,
        ):
        self.date = dt.strptime(date, '%d.%m.%Y').date()
        self.type = GradeRecord.ExamType(type)
        self.semester = semester
        self.grade = grade
        self.examiner = examiner
        self.scale = scale
        
    def __repr__(self):
       return f'<семестр: - {self.semester}, дата экзамена: {self.date}, тип экзамена: {self.type.__dict__["_value_"]}, оценка: {self.scale}, преподаватель: {self.examiner}>'
 
        
class Gradebook():
    """Зачётная книжка"""
    
    def __init__(
            self,
            id: Student,
            records: GradeRecord
    ):
        self.id = id
        self.records = records
        
    def avg_semester_grade(self) -> float:
        """Средняя оценка за семестр"""
        pass
        
    def __repr__(self):
       return f'<студент: {self.id}, экзамен: {self.records}>'    
        
# ORGANIZATION LEVEL


class OrganizationLevel(list, ABC):
    """Организационный уровень"""

    def __init__(
            self,
            title: str,
            description: str = '',
            head: Administrator = None,
            staff: list[Administrator] = [],
            contact: Contact = None
    ):
        super().__init__()
        self.title = title
        self.description = description
        self.head = head
        self._staff = staff
        self.contact = contact
        
    @property    
    def staff(self) -> list[Administrator]:
        """Персонал - getter"""
        return self._staff
    
    @staff.setter
    def staff(self, person: Person) -> None:
        """Персонал - setter"""
        self._staff.append(person)
        
    def __repr__(self):
        return f'<{self.title}>'
    
    
class Group(list):
    """Группа"""
    
    def __init__(
            self,
            id_group: str = '',
            chief: Student = None,
            curator: Teacher = None,
            students: list[Student] = []
    ):
        super().__init__()
        self.id_group = id_group
        self.chief = chief
        self.curator = curator
        if students == []:
            self.students = getattr(data, self.id_group)
        else:
            self.students = students 
        
        
    def __repr__(self):
        return f"<группа: {self.id_group}, куратор: {self.curator}, староста: {self.chief}, список студентов: {self.students}>"

@dataclass
class Auditorium:
    """Аудитория"""
    
    number: str = ''
    seats: int = 0
    building: str = ''
    
    def __repr__(self):
        return f"<аудитория: {self.number}, количество мест: {self.seats}, строение: {self.building}>"
    
    
class Department(OrganizationLevel):
    """Кафедра"""
    
    def __init__(
            self,
            title,
            description = None,
            head = None,
            staff = None,
            contact = None,
            teachers: list[Teacher] = [],
            auditoria: list[Auditorium] = []
    ):
        super().__init__(title, description, head, staff, contact)
        if teachers == []:
            self.teachers = getattr(data, self.title)
        else:
            self.teachers = teachers 
        self.auditoria = auditoria
        
    def __repr__(self):
        return f"<кафедра: {self.title}, преподаватели: {self.teachers}, кабинеты: {self.auditoria}>"


class Faculty(OrganizationLevel):
    """Факультет"""
    
    def __init__(
            self,
            title,
            description = None,
            head = None,
            staff = None,
            contact = None,
    ): 
        super().__init__(title, description, head, staff, contact)

    def __repr__(self):
        return f"<факультет {self.title}, декан: {self.head}>"
        
        
    def enroll_student(self) -> None:
        """Зачислить студента"""
        pass

   
    def expel_student(self) -> None:
        """Отчислить студента"""
        pass
        
        
# @singleton
class HR(OrganizationLevel):
    """Отдел кадров"""

    def __init__(self, title): 
        super().__init__(title)

    def hire(self):
        """Нанимать"""
        pass
    
    def fire(self):
        """Увольнять"""            
        pass
        
# @singleton
class University(OrganizationLevel):
    """Университет"""
    
    def __init__(
            self,
            title,
            description = None,
            head = None,
            staff = None,
            contact = None,
            hr: HR = None
    ):
        super().__init__(title, description, head, staff, contact)
        self.hr = hr
        
    def __repr__(self):    
        return f"<название университета: {self.title}, ректор: {self.head}, контакты: {self.contact}>"
    
    
    def change_head(self, person: Administrator) -> None:
        """Определить управляющего"""
        pass

