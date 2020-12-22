# 4. Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

words = input('Enter words: ')

wordsList = words.split(' ')

print(wordsList)

i = 0
while i < len(wordsList):
    print(wordsList[i]) if len(wordsList[i]) < 10 else print(wordsList[i][0:10])
    i += 1
