# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.
from lesson8.task4_5_6.NotOfficeEquipmentError import MyZeroDivisionError

try:
    value = int(input('Enter value: '))
    if value == 0:
        raise MyZeroDivisionError('Value cant be null')
    print(30/value)
except MyZeroDivisionError as err:
    print(err)
