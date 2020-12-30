# 4. Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

test = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def without_duplicates_gen(input_list):
    unique_list = []
    copied_list = input_list.copy()

    for el in input_list:
        if el not in unique_list:
            unique_list.append(el)

    for el in unique_list:
        copied_list.remove(el)
        if el not in copied_list:
            yield el


gen = without_duplicates_gen(test)

new_list = [el for el in gen]

print(new_list)
print(test)
