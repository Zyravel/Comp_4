import sqlite3

base_Zyrav = 'Zyr_4_base.db'
table_shaverma = 'shawerma'


def show_all(base, table):
    try:
        con = sqlite3.connect(base)
        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM {table}')
        x = cursor.fetchall()
        for lot in x:
            print('Название:', lot[1],  end = ". ")
            print('Ингридиенты: ', end = "")
            print(*lot[2:], sep = ", ", end = '.')
            print()
    except:
        print("Что-то не так(((")
    finally:
        cursor.close()
        con.close()


# show_all(base_Zyrav, table_shaverma) # пример работы функции по выводу всех записей


def show_one(base, table, name_input):
    try:
        con = sqlite3.connect(base)
        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM {table} where name = "{name_input}"')
        result = cursor.fetchone()
        if result:
            print(f"Найдено name: {result[1]}, meat: {result[2]}, bread: {result[3]}")
        else:
            print("Название не найдено")
    # except:
        # print("Что-то не так(((")
    finally:
        cursor.close()
        con.close()


# name_input = input('введите название навермы: ' ).capitalize()  # пример вывода информации по имени
# show_one(base_Zyrav, table_shaverma, name_input) 



def add_name_to_shav(base, table, name_add, meat_add, bread_add):
        try:
            con = sqlite3.connect(base)
            cursor = con.cursor()
            cursor.execute(f"INSERT INTO {table}(name, meat, bread) VALUES ('{name_add.capitalize()}', '{meat_add.lower()}', '{bread_add.lower()йцу}')")
            con.commit()
        except:
            print("Что-то не то(((")
        finally:
            cursor.close()
            con.close()


name_input = input("введите название новой шавермы: ")
meat_input = input("введите мясную составляющую: ")
bread_input = input("введназвание сдобную составляющую : ")
add_name_to_shav(base_Zyrav, table_shaverma, name_input, meat_input, bread_input) # пример добавления новой шавермы