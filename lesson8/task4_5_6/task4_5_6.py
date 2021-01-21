# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который
# будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
from Scanner import Scanner
from Fax import Fax
from Store import Store
from Printer import Printer
from random import randrange

from lesson8.task4_5_6 import NotOfficeEquipmentError
from lesson8.task4_5_6.OfficeEquipment import OfficeEquipment

scanner = Scanner(cost=120, name='Scanner Hp')
fax = Fax(cost=10, name='Fax Cannon')
printer = Printer(cost=50, name='Printer Hp laserJet')
scanner_delete = Scanner(cost=40, name='Scanner Hp_delete')
store = Store()
store.add(fax)
store.add(printer)
store.add(scanner_delete)
store.add(scanner)

print('Initial store:\n', store)
store.del_item(scanner_delete)
print('After deletion:\n', store)
store.run_all()
print('Total cost: ', store.get_total_cost())


def generate_equipment():
    for index in range(0, 100):
        equip_class = [Fax, Scanner, Printer][randrange(0, 3)]
        store.add(equip_class(cost=randrange(0, 100), name=f"Entity {index}"))


generate_equipment()

print('Stats: ', store.get_stats())
print('Total cost: ', store.get_total_cost())

try:
    store.add(2)
except NotOfficeEquipmentError:
    print('Exception work!')
