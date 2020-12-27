# 4. Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

words = input('Enter words: ')

words_list = words.split(' ')

print(words_list)


for index, value in enumerate(words_list):
    print(words_list[index][0:10])
