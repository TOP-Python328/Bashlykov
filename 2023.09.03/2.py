from decimal import Decimal as  dcm
from datetime import time, date, datetime
import numbers

class PowerMeter:
    """Описывает двухтарифный счётчик потреблённой электрической мощности"""
    def __init__(self,
            tariff1: numbers.Number = 2.89,
            tariff2: numbers.Number = 2.01,
            tariff2_starts: datetime.time = time(23,00),
            tariff2_ends: datetime.time = time(7,00)): 
        self.tariff1 = dcm(tariff1)
        self.tariff2 = dcm(tariff2)
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power: dcm = dcm(0)
        self.current_date: datetime.date = date.today().strftime("01.%m.%Y")
        self.charges: dict[datetime.date, dcm] = {self.current_date: self.power}
        
    
    def __repr__(self):
        return f'<{self.__class__.__name__} : {self.power} кВт/ч>'
        

    def __str__(self):    
        return f'({date.today().strftime("%B")}) {self.charges[self.current_date]}'
        
        
    def meter(self, power: numbers.Number) -> dcm:
        """Вычисляет и возвращает стоимость потреблённой мощности, соответствующей переданному значению потреблённой мощности"""
        power = dcm(power)
        if self.tariff2_ends < datetime.now().time() < self.tariff2_starts:
            power = self.tariff1 * power
        else:
            power = self.tariff2 * power
        self.power += power.quantize(dcm("1.00"))
        self.charges[self.current_date] += power.quantize(dcm("1.00"))
        
        return power.quantize(dcm("1.00"))
        
# C:\Users\Asus\OneDrive\Рабочий стол\Program\dz_python\Bashlykov\2023.09.03
 # 21:58:06 > python -i 2.py
# >>> pm1 = PowerMeter()
# >>> pm1.meter(2)
# Decimal('5.78')
# >>> pm1.meter(1.2)
# Decimal('3.47')
# >>>
# >>> pm1
# <PowerMeter : 9.25 кВт/ч>
# >>> print(pm1)
# (September) 9.25
# >>> pm1.charges
# {'01.09.2023': Decimal('9.25')}
# >>> pm1.power
# Decimal('9.25')