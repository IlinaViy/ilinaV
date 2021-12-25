import sqlite3
conn = sqlite3.connect('bd.db')
cursor = conn.cursor()
#вывести максимальную цену продукта
cursor.execute('SELECT MAX(price) FROM products')
print(cursor.fetchall())

#вывести id пользователей у которых день рождения сегодня
cursor.execute('SELECT id FROM users WHERE substr(birthday, 6) == substr(date("now"), 6)')
print(cursor.fetchall())

#вывести два id пользователей у которых заказы на максимальную сумму
cursor.execute('SELECT user_id FROM "order" ORDER BY sum DESC LIMIT 2')
print(cursor.fetchall())

#вывести id заказа, где присутствует продукт с ценой за штуку 15
cursor.execute('SELECT order_id FROM basket WHERE item_id = (SELECT id FROM products WHERE price=15)')
print(cursor.fetchall())

#вывести фамилию пользователя, у которого адрес доставки Осло и название товара с ценой за штуку 2
cursor.execute('SELECT lastname FROM users WHERE address="Oslo" UNION SELECT name FROM products WHERE price=2')
print(cursor.fetchall())

conn.commit()
conn.close()