import sqlite3

# def delete_client(client_id):
#     conn = sqlite3.connect('insurance_company.db')
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
#     conn.commit()
#     conn.close()
#     print(f"Клиент с ID {client_id} был успешно удален.")
#
# if __name__ == "__main__":
#     try:
#         client_id = int(input("Введите ID клиента для удаления: "))
#         delete_client(client_id)
#     except ValueError:
#         print("Ошибка: некорректный ID клиента.")


# Удаление всех таблиц
def drop_all_tables():
    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()

    tables = ['clients', 'policies', 'claims']

    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table};")

    conn.commit()
    conn.close()
    print("Все таблицы были успешно удалены.")

if __name__ == "__main__":
    drop_all_tables()