# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
import re

total = 0
amount = 1

try:
    with open("file.txt", ) as f_obj:
        for line in f_obj:
            salary = 0
            value = re.split(':', line.rstrip())
            try:
                salary = int(value[1])
            except ValueError:
                print(salary)
            total += salary
            amount += 1
            if salary >= 20000:
                print(value[0])
except IOError:
    print("Произошла ошибка ввода-вывода!")

print(f'average salary: {total / amount}')
