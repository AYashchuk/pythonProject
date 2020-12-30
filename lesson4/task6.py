# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle


def numbers_count_gen(start):
    res = []
    for el in count(start):
        if el > 10:
            break
        else:
            res.append(el)
    return res


def numbers_cycle_gen(input_list):
    index = 0
    res = []
    for el in cycle(input_list):
        if index > 10:
            break
        res.append(el)
        index += 1
    return res


print(numbers_count_gen(3))
print(numbers_cycle_gen([1, 2, 3, 4]))
