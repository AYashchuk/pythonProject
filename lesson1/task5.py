# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

a = int(input("Выручка: "))
b = int(input("Bздержекa: "))

if a - b > 0:
    print("Прибыль!")
    print("Рентабельность {0}".format((a - b)/a))
    amount = int(input("Количество сотрудников: "))
    print("Прибыль на одного сотрудника: {0}".format((a-b)/amount))
else:
    print("Убыток")