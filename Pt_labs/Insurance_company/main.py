# Является основным для запуска приложения, где объединяются все части
from db_connection import create_connection
from models import create_tables
from data_operations import insert_data
from queries import select_clients_with_policies, select_claims_summary, select_total_claims_amount

def main():
    # Путь к файлу базы данных
    database = "insurance_company.db"

    # Создание соединения с базой данных
    try:
        conn = create_connection(database)
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return

    # Выбор действия
    action = input("Выберите действие: 1 - Создать таблицы, 2 - Вставить данные, 3 - Выполнить запросы: ")

    try:
        if action == '1':
            # Создание таблиц
            create_tables(conn)
            print("Таблицы созданы.")
        elif action == '2':
            # Вставка данных
            insert_data(conn)
            print("Данные вставлены.")
        elif action == '3':
            # Выполнение запросов
            clients_with_policies = select_clients_with_policies(conn)
            claims_summary = select_claims_summary(conn)
            total_claims_amount = select_total_claims_amount(conn)

            # Вывод результатов
            print("Клиенты с количеством полисов:")
            for client in clients_with_policies:
                print(client)

            print("\nСводка по заявкам:")
            for claim in claims_summary:
                print(claim)

            print(f"\nОбщая сумма заявок: {total_claims_amount[0]}")
        else:
            print("Неверный выбор.")
    except Exception as e:
        print(f"Ошибка при выполнении действия: {e}")
    finally:
        # Закрытие соединения
        if conn:
            conn.close()
            print("Соединение с SQLite закрыто.")

if __name__ == "__main__":
    main()