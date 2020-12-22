# 3 Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
year = [
    ['winter', 'winter', 'spring'],
    ['spring', 'spring', 'summer'],
    ['summer', 'summer', 'autumn'],
    ['autumn', 'autumn', 'winter']
]

monthDict = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter'
}


monthNumber = int(input('Enter number of month: ')) % 12

print(f"Its {monthDict[monthNumber]}")

print(f"Its {year[monthNumber // 4][(monthNumber -1) % 3]}")
