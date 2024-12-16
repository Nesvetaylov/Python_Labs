#!/usr/bin/env python3

import cgi
import cgitb
from db_connection import create_connection
from queries import select_clients_with_policies

cgitb.enable()

def main():
    print("Content-Type: text/html")
    print()

    database = "insurance_company.db"
    conn = create_connection(database)
    clients_with_policies = select_clients_with_policies(conn)
    conn.close()

    print("<h1>Клиенты с полисами</h1>")
    print("<table border='1'><tr><th>Имя</th><th>Количество полисов</th></tr>")
    for client in clients_with_policies:
        print(f"<tr><td>{client[0]}</td><td>{client[1]}</td></tr>")
    print("</table>")

if __name__ == "__main__":
    main()