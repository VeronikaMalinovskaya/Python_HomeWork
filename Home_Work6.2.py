#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19
#n = [1.1 1.2 3.1 10.01]

#def average(n):
    #max = 0
    #min = 1  
    #for i in n:
        #temp = round(i % 1, 3) 
        #if temp > max:
            #max = temp
        #elif temp < min:
            #min = temp
    #print(f"max {max} min {min}")
    #res = max - min
    #return res

#print(average(n))

# Вариант с использованием map, lambda и list comprehension 

input_list = list(map(lambda x: float(x), input("Введите число чер пробел : ").split()))
lst = [round(i % 1, 2) for i in input_list if i % 1 != 0]
print(f"Список вещественных чисел : {input_list}\nразница между max и min: {max(lst) - min(lst)}")