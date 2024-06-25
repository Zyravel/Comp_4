import sqlite3


base_Zyrav = 'Zyravel_4.db'
table_shaverma = 'Shaverma'


def show_all(base, table):
    try:
        con = sqlite3.connect(base)

        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM {table}')
        x = cursor.fetchall()
        for lot in x:
            print('Название:', lot[1],  end = ". ")
            print('Ингридиенты:', *lot[2:], sep = ", ", end = '.')
            print()
    except:
        print("Что-то не то(((")
    finally:
        cursor.close()
        con.close()


# show_all(base_Zyrav, table_shaverma) # пример работы функции по выводу всех записей


def add_name_shav(base, table, name_add, meat_add, bread_add):
        try:
            con = sqlite3.connect(base)

            cursor = con.cursor()
            cursor.execute(f"INSERT INTO {table}(name, meat, bread) VALUES ({name_add}, {meat_add}, {bread_add})")
            # print(f"INSERT INTO {table}(name, meat, bread) VALUES ({name_add}, {meat_add}, {bread_add})")

            # x = cursor.fetchall()
            # for i in x:
            #     print(i)
        # except:
        #     print("Что-то не то(((")
        finally:
            cursor.close()
            con.close()

add_name_shav(base_Zyrav, table_shaverma, 'хотплейт', 'курица', 'пита')