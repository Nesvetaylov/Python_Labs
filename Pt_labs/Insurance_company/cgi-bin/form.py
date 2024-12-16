#!/usr/bin/env python3

import cgi
import cgitb
from db_connection import create_connection

cgitb.enable()  # Включает отладку ошибок

def main():
    print("Content-Type: text/html")  # Заголовок
    print()  # Пустая строка для завершения заголовка

    # Обработка формы
    form = cgi.FieldStorage()
    name = form.getvalue('name')
    email = form.getvalue('email')

    if name and email:
        database = "insurance_company.db"
        conn = create_connection(database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()
        print(f"<h1>Клиент {name} успешно добавлен!</h1>")
    else:
        print("<h1>Ошибка: имя и email обязательны для заполнения.</h1>")

if __name__ == "__main__":
    main()