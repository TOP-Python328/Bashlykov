# ИСПОЛЬЗОВАТЬ: общепринятым сокращением Decimal является dec
from decimal import Decimal as dec
from datetime import time, date, datetime
# ИСПОЛЬЗОВАТЬ: в задании я пишу квалифицированное имя класса, включающее модуль, чтобы вы не запутались в библиотеках — к импорту это никак не относится, из стандартной библиотеки по-прежнему берём всё с помощью from ... import ...
from numbers import Number


class PowerMeter:
    """Описывает двухтарифный счётчик потреблённой электрической мощности"""
    def __init__(
            self,
            tariff1: Number = 2.89,
            tariff2: Number = 2.01,
            # ИСПРАВИТЬ: а я ведь говорил: не запутайтесь между модулем и классом — вот вы и запутались, сейчас идентификатор datetime ссылается на объект класса, а не модуля, и только специфическая структура конкретно этих классов уберегла вас от исключения
            tariff2_starts: datetime.time = time(23,00),
            tariff2_ends: datetime.time = time(7,00)
    ):
        self.tariff1 = dec(tariff1)
        self.tariff2 = dec(tariff2)
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power: dec = dec(0)
        # ИСПРАВИТЬ: во-первых, этот атрибут нигде не обновляется, а значит речь идёт не о "текущей дате", а о "дате создания"; во-вторых, такой атрибут скорее мешает, чем помогает (см. комментарий к __str__())
        self.current_date: datetime.date = date.today().strftime("01.%m.%Y")
        self.charges: dict[datetime.date, dec] = {self.current_date: self.power}

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.power} кВт/ч>'

    def __str__(self):
        # ИСПРАВИТЬ: если я через месяц после создания экземпляра запрошу строковое представление данного счётчика, то увижу данные за всё тот же первый месяц — это вряд ли соответствует замыслу
        return f'({date.today().strftime("%b")}) {self.charges[self.current_date]}'

    def meter(self, power: Number) -> dec:
        """Вычисляет и возвращает стоимость потреблённой мощности, соответствующей переданному значению потреблённой мощности"""
        power = dec(power)
        if self.tariff2_ends < datetime.now().time() < self.tariff2_starts:
            power = self.tariff1 * power
        else:
            power = self.tariff2 * power
        self.power += power.quantize(dec("1.00"))
        self.charges[self.current_date] += power.quantize(dec("1.00"))
        
        return power.quantize(dec("1.00"))


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


# ИТОГ: хорошо, доработайте немного — 4/6
