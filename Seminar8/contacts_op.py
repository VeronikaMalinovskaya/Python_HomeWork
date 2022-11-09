from asyncio import create_subprocess_shell
from dataclasses import dataclass
from operator import concat
from os.path import exists


def write_contact(user, data):
    data.append(user)


def write_data(data, columns):
    with open(FILE_NAME, "w", encoding="UTF-8") as f:
      f.write(", ".join(columns) + "\n")
      for user in data: 
        f.write(", ".join(user.values()) + "\n")


def add_column(data, column, columns):
    for user in data: 
        user[column] = "None"  # для имеющихся пользователей прописываем none в данных нового столбца, где пусто
    columns.append(column)
    return data
        

def read_data():
    valid = exists(FILE_NAME)
    if not valid: 
        return []
    with open(FILE_NAME, "r", encoding="UTF-8") as f: 
        data = f.read()
        if "\n" not in data:
            return []
        columns = data.split("\n")[0].strip().split(", ")  # строка с заголовком 
        data = [{columns[i]: user.strip().split(", ")[i] if user else "" for i in range(len(columns))} for user in data.split("\n")[1:] if user]
        return data


def get_columns(data):
    if not data: 
        return ["Фамилия", "Имя"]
    columns = list(data[0].keys())
    return columns


def find_contact(data, columns):
    column = input("Введите столбец поиска: ")
    val = input("Введите значение для поиска: ")
    flag = False
    for user in data:
        if column not in columns:
            return print("\nТакого столбца нет!")
        if user[column] == val: 
            print(user)
            flag = True
    if not flag: 
        print("\nДанные не найдены!")


def upd_contact(data, columns):
    column = input("Введите столбец поиска: ")
    val = input("Введите значение для поиска: ")
    var = input("Введите редактируемое поле: ")
    flag = False
    for user in data:
        if column not in columns:
            return print("\nТакого столбца нет!")
        if user[column] == val: 
            var1 = input("Введите данные: ")
            confirm = input("\nВыберите 1 для сохранения изменений или нажмите любую клавишу для возврата в меню: ")
            if confirm == "1":
                user[var] = var1
            print(user)
            flag = True
            break
    if not flag: 
        print("\nДанные не найдены!")


def del_contact(data, columns):
    column = input("Введите столбец поиска: ")
    val = input("Введите значение для поиска: ")
    flag = False
    for user in data:
        if column not in columns:
            return print("\nТакого столбца нет!")
        elif user[column] == val:
            confirm = input("\nВыберите 1 для сохранения изменений или нажмите любую клавишу для возврата в меню: ")
            if confirm == "1":
                data.remove(user)
        flag = True
    if not flag:
        print("\nДанные не найдены!")


FILE_NAME = "data_base.csv"