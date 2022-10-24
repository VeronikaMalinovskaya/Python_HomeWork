#Задача: предложить улучшения кода для уже решённых задач:
#С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:*
#6782 -> 23
#0,56 -> 11
#n = int(input("Введите число: "))
 
#suma = 0 
#while n > 0:
    #digit = n % 10
    #suma = suma + digit
    #n = n // 10
 #print("Сумма цифр :", suma)
 
 # Вариант с использованием list comprehension
 
n = input("Введите число: ")
suma = sum([int(digit) for digit in n if digit.isdigit()])
print(suma)
 
