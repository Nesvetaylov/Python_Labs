# Содержит SQL-запросы для создания таблиц
from db_connection import execute_query  # Импортируем функцию для выполнения запросов

# Таблица клиентов
def create_tables(conn):
    try:
        create_clients_table = """
        CREATE TABLE IF NOT EXISTS Clients (
            ClientID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email TEXT NOT NULL,
            Phone TEXT NOT NULL
        );
        """
        # Таблица полисов
        create_policies_table = """
        CREATE TABLE IF NOT EXISTS Policies (
            PolicyID INTEGER PRIMARY KEY AUTOINCREMENT,
            ClientID INTEGER,
            PolicyType TEXT NOT NULL,
            StartDate TEXT NOT NULL,
            EndDate TEXT NOT NULL,
            FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
        );
        """
        # Таблица заявок
        create_claims_table = """
        CREATE TABLE IF NOT EXISTS Claims (
            ClaimID INTEGER PRIMARY KEY AUTOINCREMENT,
            PolicyID INTEGER,
            ClaimDate TEXT NOT NULL,
            Amount REAL NOT NULL,
            Status TEXT NOT NULL,
            FOREIGN KEY (PolicyID) REFERENCES Policies(PolicyID)
        );
        """
        
        # Выполнение запросов на создание таблиц
        execute_query(conn, create_clients_table)
        execute_query(conn, create_policies_table)
        execute_query(conn, create_claims_table)
        
        print("Таблицы успешно созданы.")
        
    except Exception as e:
        print(f"Ошибка при создании таблиц: {e}")