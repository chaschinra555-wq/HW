file = open('text.txt', 'w')

text = input('Введите текст: ')
file.write(text)

file.close()