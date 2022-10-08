#Даны два файла, в каждом из которых находится запись многочлена. 
#Задача - сформировать файл, содержащий сумму многочленов.
from importlib.resources import path
import re
import itertools


first_file = '33_Polynomial.txt'
second_file = '33_Polynomial2.txt'
file_sum = '34_Sum_polynomial.txt'

# Получение данных из файла, тип строка

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

# Получение списка кортежей каждого (<коэффициент>, <степень>)

def convert_pol(poly):
    poly = poly.replace('= 0', '') # убираем знак = и 0, путем замены на ''
    print(poly)
    poly = re.sub("[*]", " ", poly).split('+') # убираем знак * и **, путем замены на ''
    # разбиваем на строки по символу +
    print(poly)
    poly = [char.split(' ') for char in poly] # разбиваем по-символьно на строки предыдущие строки
    # разделителем является ' '
    print(poly)
    poly = [[x for x in list if x] for list in poly] # убираем пробелы из наших списков
    print(poly)
    # получаем список кортежей, состоящих из коэфициента и степени
    for i in poly:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    print(poly)
    poly = [tuple(int(x) for x in j if x != 'x') for j in poly]
    print(poly)
    return poly

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)
# теперь нам надо сложить цифры, не трогая степени
def fold_pols(pol1, pol2):   
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

# Составление итогового многочлена

def get_sum_pol(pol):
    var = ['*x**'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x**': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

pol1 = read_pol(first_file)
pol2 = read_pol(second_file)
pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
write_to_file(file_sum, pol_sum)

print(pol1)
print(pol2)
print(pol_sum)