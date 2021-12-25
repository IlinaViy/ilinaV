import sqlite3
conn = sqlite3.connect('bd.db')
cursor = conn.cursor()
#������� ������������ ���� ��������
cursor.execute('SELECT MAX(price) FROM products')
print(cursor.fetchall())

#������� id ������������� � ������� ���� �������� �������
cursor.execute('SELECT id FROM users WHERE substr(birthday, 6) == substr(date("now"), 6)')
print(cursor.fetchall())

#������� ��� id ������������� � ������� ������ �� ������������ �����
cursor.execute('SELECT user_id FROM "order" ORDER BY sum DESC LIMIT 2')
print(cursor.fetchall())

#������� id ������, ��� ������������ ������� � ����� �� ����� 15
cursor.execute('SELECT order_id FROM basket WHERE item_id = (SELECT id FROM products WHERE price=15)')
print(cursor.fetchall())

#������� ������� ������������, � �������� ����� �������� ���� � �������� ������ � ����� �� ����� 2
cursor.execute('SELECT lastname FROM users WHERE address="Oslo" UNION SELECT name FROM products WHERE price=2')
print(cursor.fetchall())

conn.commit()
conn.close()