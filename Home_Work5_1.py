#Напишите программу, удаляющую из текста все слова, содержащие ""абв""

text = input("Введите текст через пробел: ")

print('Исходный текст: ', text)
text_word = text.split()
find = 'абв'
new_text = []

for i in text_word:
    if find not in i:
        new_text.append(i)

text_2 = ' '.join(new_text) 
print('Полученный текст: ', text_2)