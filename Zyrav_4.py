import sqlite3
import random


base_Zyrav = 'Zyr_4_base.db'
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


def show_one(base, table):  # выводит одну запись по имени
    try:
        name_input = input('введите название навермы: ' ).capitalize()
        con = sqlite3.connect(base)
        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM {table} where name = "{name_input}"')
        result = cursor.fetchone()
        if result:
            print(f"Найдено name: {result[1]}, meat: {result[2]}, bread: {result[3]}")
        else:
            print("Название не найдено")
    except:
        print("Что-то не так(((")
    finally:
        cursor.close()
        con.close()


def add_name_to_shav(base, table):  # добавляет новую запись
    try:
        name_add = input("введите название новой шавермы: ").capitalize()
        meat_add = input("введите мясную составляющую: ").lower()
        bread_add = input("введназвание сдобную составляющую : ").lower()

        con = sqlite3.connect(base)
        cursor = con.cursor()
        cursor.execute(f"INSERT INTO {table}(name, meat, bread) VALUES ('{name_add}', '{meat_add}', '{bread_add}')")
        con.commit()
    except:
        print("Что-то не то(((")
    finally:
        cursor.close()
        con.close()


con = sqlite3.connect(base_Zyrav)   
cursor = con.cursor()
# cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_shaverma} (
# id INTEGER PRIMARY KEY,
# name TEXT UNIQUE NOT NULL,
# meat TEXT NOT NULL,
# bread TEXT NOT NULL
# )''')   # создание таблицы шаверма


# cursor.execute(f"INSERT INTO {table_shaverma}(name, meat, bread) VALUES ('Классика', 'курица', 'лаваш')") # тестовое заполнение таблицы
# cursor.execute(f"INSERT INTO {table_shaverma}(name, meat, bread) VALUES ('Хот-дог', 'сосиски', 'пита')")
# cursor.execute(f"INSERT INTO {table_shaverma}(name, meat, bread) VALUES ('Кебаб-ролл', 'кебаб', 'лаваш')")


# add_name_to_shav(base_Zyrav, table_shaverma) # добавление новой записи
# show_all(base_Zyrav, table_shaverma) # вывод всех записей
# show_one(base_Zyrav, table_shaverma) # вывод информации по имени


# try:
#     cursor.execute(f"ALTER TABLE {table_shaverma} ADD ready int NOT NULL DEFAULT 0 ")  #  столбец для отображения выполненных и невыполненных заказов
#     con.commit()
#     cursor.execute(f'SELECT * FROM {table_shaverma}')
#     x = cursor.fetchall()
#     for row in range(len(x)):  
#         num = random.randint(0, 1)
#         cursor.execute(f"UPDATE {table_shaverma} SET ready = {num} WHERE id = {row}") # рандомное заполнение столбца 
#         con.commit()
# except:
#     print("Что-то не то(((")


# cursor.execute(f"SELECT ready, COUNT(*) FROM {table_shaverma} GROUP BY ready ORDER BY ready ") # количестово выполненных и невыполненных заказов
# x = cursor.fetchall()
# if len(x) > 0:
#     result = {0: 'не выполнено', 1: 'выполнено'}
#     for i in x:
#         print('Заказов', result[i[0]], i[1]) # выводит гоовность и количество заказов


# cursor.execute(f"DELETE FROM {table_shaverma} WHERE ready = 1") # удаление выполненных заказов

con.commit()
cursor.close()
con.close()



    

