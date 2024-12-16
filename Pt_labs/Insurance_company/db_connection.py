# Содержит функции для создания соединения с базой данных
import sqlite3

def create_connection(db_file):
    """Создает соединение с SQLite базой данных."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Соединение с SQLite успешно установлено.")
    except sqlite3.Error as e:
        print(f"Ошибка '{e}' произошла при подключении к SQLite.")
    return conn
def execute_query(conn, query):
    """Выполняет SQL-запрос."""
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()  # Подтверждаем изменения в базе данных
        print("Запрос выполнен успешно.")
    except sqlite3.Error as e:
        print(f"Ошибка при выполнении запроса: '{query}' - {e}")
