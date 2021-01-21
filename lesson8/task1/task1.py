# Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.

# Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число».

# Второй,с декоратором @staticmethod, должен проводить валидацию (проверку на корректность)
# числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
from Date import Date

date = Date("23-01-2020")
date_invalid_day = Date('30-02-2020')
date_invalid_moth = Date('1-13-2020')
date_invalid_year = Date('1-02--1')

print("Parsed date: ", Date.parse_date(date))
print("Check valid date: ", Date.validate_date(date))
print("Check date with invalid day: ", Date.validate_date(date_invalid_day))
print("Check date with invalid day: ", Date.validate_date(date_invalid_moth))
print("Check date with invalid year: ", Date.validate_date(date_invalid_year))
