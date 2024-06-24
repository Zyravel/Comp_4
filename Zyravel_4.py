import sqlite3


con = sqlite3.connect('Zyravel_4.db')
cursor = con.cursor()
res = cursor.execute('select * from Shaverma')
x = res.fetchall()
print(x)

cursor.close()
con.close()