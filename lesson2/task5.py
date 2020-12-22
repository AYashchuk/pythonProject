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
  _list = {}

  def __init__(self, source):
      for val in source:
          self.append(val)

  def __toList__(self):
      res = []
      for key in sorted(self._list, reverse=True):
          elem = self._list.get(key)
          if elem == 0:
              res.append(key)
          else:
              while elem >= 0:
                  res.append(key)
                  elem = elem - 1
      return res

  def __repr__(self):
    return f"{self.__toList__()}"

  def append(self, number):
      value = self._list.get(number, -1)
      if value == -1:
          self._list.update({number: 0})
      else:
          self._list.update({number: value + 1})


initialList = [7, 5, 3, 3, 2]
a = Rating(initialList)
a.append(3)
print(a)
