# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input("Введите время в секундах: "))
secInHour = 60 * 60
hours = time // secInHour
minutes = (time - (hours * secInHour)) // 60 if hours > 0 else time // 60
seconds = time % 60

formattedHours = hours if hours % 10 > 0 else "0{0}".format(hours)
formattedMinutes = minutes if minutes % 10 > 0 else "0{0}".format(minutes)
formattedSeconds = seconds if seconds % 10 > 0 else "0{0}".format(seconds)

print("{0}.{1}.{2}".format(formattedHours, formattedMinutes, formattedSeconds))
