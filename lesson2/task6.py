# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
from collections import defaultdict

class Products:
    _products = []

    def add(self, product):
        self._products.append((len(self._products), product))

    def __str__(self):
        res = ''
        for elem in self._products:
            res += f"{elem}"
        return f"{res}"

    def get_analytics(self):
        res = defaultdict(list)
        for elem in self._products:
            target_product = elem[1]
            for key in sorted(target_product):
                value = res[key]
                value.append(target_product[key])

        return res


products = Products()
count = 1
try:
    count = int(input('Enter amount of products: '))
except:
    print('Entered value inst int type')

for i in range(0, count):
    print(f"Enter data for {i + 1} product")
    name = input('Enter products name: ')
    cost = input('Enter products cost: ')
    amount = input('Enter products amount: ')
    unit = input('Enter products unit: ')
    products.add({"name": name, "cost": cost, "amount": amount, "unit": unit})
    i += 1

print(products.get_analytics())
print(products.get_analytics2())
