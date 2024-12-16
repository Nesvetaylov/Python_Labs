# Содержит функции для вставки данных в таблицы
from db_connection import execute_query  # Импортируем функцию для выполнения запросов

def insert_data(conn):
    """Заполняет таблицы данными."""
    insert_clients = """
    INSERT INTO Clients (Name, Email, Phone) VALUES
    ('Иван Иванов', 'ivan@example.com', '123456789'),
    ('Петр Петров', 'petr@example.com', '987654321'),
    ('Светлана Светлова', 'svetlana@example.com', '456123789');
    """
    
    insert_policies = """
    INSERT INTO Policies (ClientID, PolicyType, StartDate, EndDate) VALUES
    (1, 'Автострахование', '2023-01-01', '2024-01-01'),
    (2, 'Медицинская страховка', '2023-02-01', '2024-02-01'),
    (1, 'Страхование жилья', '2023-03-01', '2024-03-01');
    """
    
    insert_claims = """
    INSERT INTO Claims (PolicyID, ClaimDate, Amount, Status) VALUES
    (1, '2023-05-01', 5000.00, 'Ожидает рассмотрения'),
    (2, '2023-06-15', 1500.00, 'Одобрено'),
    (3, '2023-07-20', 3000.00, 'Отклонено');
    """
    
    execute_query(conn, insert_clients)
    execute_query(conn, insert_policies)
    execute_query(conn, insert_claims)