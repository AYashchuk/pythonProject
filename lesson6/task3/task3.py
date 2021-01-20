# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с
# учетом премии (get_total_income). Проверить работу примера на реальных
# данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

from Position import Position

andrew = Position("andrew", "surname 1", "dev", {"wage": 1000, "bonus": 100})
sara = Position("sara", "surname 2", "ba", {"wage": 800, "bonus": 200})

print(f"{andrew.get_full_name()}: income: {andrew.get_total_income()}")
print(f"{sara.get_full_name()}: income: {sara.get_total_income()}")
