from datetime import datetime as dt
from enum import Enum
from random import randrange as rr, sample
from pathlib import Path
from sys import path
from string import ascii_lowercase as letters

class Operation(Enum):
    PRINT_MSG = 'print_msg'
    PRINT_NUMS = 'print_nums'
    

class Logger:
    default_log_path: str | Path = Path(path[0]) / '5.log'

    @classmethod
    def append_log(cls, data: str, log_path: str | Path = None):
        if not log_path:
            log_path = cls.default_log_path
        with open(log_path, 'a', encoding='utf-8') as fileout:
            fileout.write(f'{dt.now():%Y-%m-%d %H:%M:%S} — {data}\n')
            
            
class TestCase:

    """Адресат."""
    
    def __init__(self):
        self.messages = [
            ''.join(sample(letters, k=rr(3, 7)))
            for _ in range(1000)
        ]
        self.numbers = [
            (rr(10, 100) for _ in range(rr(4, 6))) 
            for _ in range(1000)
        ]
    
    def print_msg(self):
        msg = self.messages.pop()
        print(msg)
    
    def print_nums(self):
        nums = self.numbers.pop()
        print(*nums)
        

class TestCommand:
  
    """Команда."""    
    def __init__(
            self,
            account: TestCase,
            operation: Operation,
   ):
        self.account = account
        self.operation = operation
        self.success: bool = False

    def __log(self, *, undo: bool = False) -> None:
        if undo:
            data = 'UNDO'
        else:
            data = 'OK'
        data += f'— {self.operation.name}'
        Logger.append_log(data)
   
    def execute(self) -> None:
    
        """Выполняет операцию"""
        if not self.success:
            if self.operation is Operation.PRINT_MSG:
                self.account.print_msg()
            elif self.operation is Operation.PRINT_NUMS:
                self.account.print_nums()
            self.success = True
            self.__log()
            

    def undo(self) -> None:
    
        """Отменяет операцию"""
        if self.success:
            if self.operation is Operation.PRINT_MSG:
                self.account.print_nums()
            elif self.operation is Operation.PRINT_NUMS:
                self.account.print_msg()
            self.success = False
            self.__log(undo=True)
            
    def re_undo(self) -> None:
    
        """Повторное выполнения отменённых операций"""
        
        self.execute()      

# C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24
 # 20:35:16 > python -i 5.py
# >>> test = TestCase()
# >>> c1 = TestCommand(test,  Operation.PRINT_MSG)
# >>> c1.execute()
# wuz
# >>> c1.execute()
# >>> c1.undo()
# 54 58 12 10 66
# >>> c1.execute()
# yvkwu
# >>> c1.undo()
# 29 10 14 53
# >>> c1.re_undo()
# iaf
# >>> c1.re_undo()
# >>> c2 = TestCommand(test,  Operation.PRINT_NUMS)
# >>> c2.execute()
# 66 49 13 65
# >>> c2.undo()
# ubpdf
# >>> c2.re_undo()
# 84 39 21 26 19