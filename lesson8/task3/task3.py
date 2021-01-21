# 3. Создайте собственный класс-исключение,
# который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка


class OnlyNumbersList:
    def __init__(self):
        self.numbers = []

    def fill_array(self):
        while True:
            value = input('Entre value: ')
            if value == 'stop':
                return
            try:
                self.numbers.append(int(value))
            except ValueError:
                print(f'value: "{value}" isn`t integer type')

    def __str__(self):
        return f"{self.numbers}"


number = OnlyNumbersList()
number.fill_array()
print(number)
