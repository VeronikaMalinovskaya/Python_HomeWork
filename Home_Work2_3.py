#3.Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#Пример:*
#Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}

#n = int(input('Введите число N '))

#lst = [round((1+1/i)**i, 2) 
#for i in range(1, n+1)]

#print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 2)}')


#Вариант с использованием функции zip
n = int(input("Введите число N: "))
list= [i for i in range(1, n+1)]
lst= [round ((1 + 1/i)**i, 2) for i in range (1, n+1)]
print(f"Для N = {n}: {dict(zip(list, lst))}")