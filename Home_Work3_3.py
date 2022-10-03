#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19
n = [1.1, 1.2, 3.1, 10.01]

def average(n):
    max = 0
    min = 1  
    for i in n:
        temp = round(i % 1, 3) 
        if temp > max:
            max = temp
        elif temp < min:
            min = temp
    print(f"max {max} min {min}")
    res = max - min
    return res


print(average(n))
