from contacts_op import get_columns
from input_data import add_contact, input_column
from contacts_op import find_contact, read_data, add_column, write_data, upd_contact, del_contact


def user_interface():
    data = read_data()
    columns = get_columns(data)
    flag = True
    print("\n***** Добро пожаловать в базу данных! *****")
    while flag: 
        print("\nВыберите пункт меню для продолжения:")
        while True:
            print("1 - Найти контакт")
            print("2 - Добавить контакт")
            print("3 - Показать все контакты")
            print("4 - Добавить столбец")
            print("5 - Редактировать контакт")
            print("6 - Удалить контакт")
            print("7 - Выход")
            choice = input()
            if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
                print("!!Выбран неверный пункт меню!!\nПопробуйте ещё раз")
                continue
            if choice == "1": 
                find_contact(data, columns)
                break
            elif choice == "2":
                add_contact(data, columns)
                break
            elif choice == "3":
                print(columns)
                print(data)
                break
            elif choice == "4":
                column = input_column()
                data = add_column(data, column, columns)
                break
            elif choice == "5":
                upd_contact(data, columns)
                break
            elif choice == "6":
                del_contact(data, columns)
                break
            else: 
                flag = False
                write_data(data, columns)
                break
