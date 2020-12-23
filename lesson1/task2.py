# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input("Введите время в секундах: "))
secInHour = 60 * 60
hours = time // secInHour
minutes = (time - (hours * secInHour)) // 60 if hours > 0 else time // 60
seconds = time % 60

print(f'{hours:02d}.{minutes:02d}.{seconds:02d}')

