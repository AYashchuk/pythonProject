# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_to_string(name, surname='', year=1980, city='', email='', phone=''):
    return f"name: {name}, surname: {surname}, year: {year}, city: {city}, email: {email}, phone: {phone}"


print(user_to_string('Andrew', year=1990, phone='+38093555555'))
