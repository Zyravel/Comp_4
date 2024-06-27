import sqlite3
from random import randint


base_Zyrav = 'Zyr_4_base.db'

# con = sqlite3.connect(base_Zyrav)   # создание таблицы
# cursor = con.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS 'shawerma' (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# meat TEXT NOT NULL,
# bread TEXT NOT NULL
# )
# ''')


table_shaverma = 'shawerma'


def show_all(base, table):  # выводит все записи
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


def show_one(base, table, name_input):  # выводит одну запись по имени
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


def add_name_to_shav(base, table, name_add, meat_add, bread_add):  # добавляет новую запись
        try:
            con = sqlite3.connect(base)
            cursor = con.cursor()
            cursor.execute(f"INSERT INTO {table}(name, meat, bread) VALUES ('{name_add.capitalize()}', '{meat_add.lower()}', '{bread_add.lower()}')")
            con.commit()
        except:
            print("Что-то не то(((")
        finally:
            cursor.close()
            con.close()




# show_all(base_Zyrav, table_shaverma) # пример работы функции по выводу всех записей

# name_input = input('введите название навермы: ' ).capitalize()  # пример вывода информации по имени
# show_one(base_Zyrav, table_shaverma, name_input) 

# name_input = input("введите название новой шавермы: ")
# meat_input = input("введите мясную составляющую: ")
# bread_input = input("введназвание сдобную составляющую : ")
# add_name_to_shav(base_Zyrav, table_shaverma, name_input, meat_input, bread_input) # пример добавления новой шавермы



con = sqlite3.connect(base_Zyrav)
cursor = con.cursor()
# cursor.execute(f"ALTER TABLE {table_shaverma} ADD ready int NOT NULL DEFAULT 0 ")  #  столбец для отображения выполненных и невыполненных заказов
# con.commit()
cursor.execute(f'SELECT * FROM {table_shaverma}')
x = cursor.fetchall()

# for row in range(len(x)):  
#     num = random.randint(0, 1)
#     cursor.execute(f"UPDATE {table_shaverma} SET ready = {num} WHERE id = {row}") # рандомное заполнение столбца 
#     con.commit()

cursor.execute(f"SELECT ready, COUNT(*) FROM {table_shaverma} GROUP BY ready ORDER BY ready ") # количестово выполненных и невыполненных заказов
x = cursor.fetchall()
# if len(x) > 0:
#     result = {0: 'не выполнено', 1: 'выполнено'}
#     for i in x:
#         print('Заказов', result[i[0]], i[1]) # выводит гоовность и количество заказов


cursor.execute(f"DELETE FROM {table_shaverma} WHERE ready = 1") # удаление выполненных заказов


con.commit()
cursor.close()
con.close()



    

