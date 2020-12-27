# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

class Rating:
    _dict = None

    def __init__(self, source):
        self._dict = {}
        for val in source:
            self.append(val)

    def __toList__(self):
        res = []
        for key in sorted(self._dict, reverse=True):
            elem = self._dict.get(key)
            while elem >= 0:
                res.append(key)
                elem = elem - 1
        return res

    def __str__(self):
        return f"{self.__toList__()}"

    def append(self, number):
        value = self._dict.get(number, -1)
        if value == -1:
            self._dict.update({number: 0})
        else:
            self._dict.update({number: value + 1})


# initialList = [7, 5, 3, 3, 2]
# a = Rating(initialList)
# a.append(3)
# print(a)


class Rating2:
    _list = None

    def __init__(self, source):
        self._list = source

    def __str__(self):
        return f"{self._list}"

    def append(self, number):
        index = self.get_index(number)
        self._list.insert(index, number)

    def get_index(self, value):
        found_index = -1
        for index, element in enumerate(self._list):
            if found_index == -1:
                if element == value:
                    found_index = index
                elif element < value:
                    found_index = index
        return found_index


initial_list = [7, 5, 3, 3, 2]
a = Rating2(initial_list)
a.append(6)
print(a)