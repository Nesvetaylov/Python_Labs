import sqlite3

# Создание базы данных и таблиц
def create_database():
    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()

    # Создание таблицы клиентов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    ''')

    # Создание таблицы полисов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS policies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        policy_number TEXT NOT NULL UNIQUE,
        policy_type TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        FOREIGN KEY (client_id) REFERENCES clients (id)
    )
    ''')

    # Создание таблицы заявлений
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS claims (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        policy_id INTEGER,
        claim_date TEXT NOT NULL,
        amount REAL NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (policy_id) REFERENCES policies (id)
    )
    ''')

    conn.commit()
    conn.close()

create_database()