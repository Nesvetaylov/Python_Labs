import sqlite3

def insert_data():
    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()

    # Вставка клиентов
    cursor.execute("INSERT INTO clients (name, email) VALUES ('Иван Иванов', 'ivan@example.com')")
    cursor.execute("INSERT INTO clients (name, email) VALUES ('Петр Петров', 'petr@example.com')")
    cursor.execute("INSERT INTO clients (name, email) VALUES ('Светлана Смирнова', 'svetlana@example.com')")
    cursor.execute("INSERT INTO clients (name, email) VALUES ('Алексей Кузнецов', 'alexey@example.com')")
    cursor.execute("INSERT INTO clients (name, email) VALUES ('Мария Васильева', 'maria@example.com')")

    # Вставка полисов
    cursor.execute("INSERT INTO policies (client_id, policy_number, policy_type, start_date, end_date) VALUES (1, 'POL123', 'Автострахование', '2023-01-01', '2024-01-01')")
    cursor.execute("INSERT INTO policies (client_id, policy_number, policy_type, start_date, end_date) VALUES (2, 'POL456', 'Медицинская страховка', '2023-02-01', '2024-02-01')")
    cursor.execute("INSERT INTO policies (client_id, policy_number, policy_type, start_date, end_date) VALUES (3, 'POL789', 'Страхование жилья', '2023-03-01', '2024-03-01')")
    cursor.execute("INSERT INTO policies (client_id, policy_number, policy_type, start_date, end_date) VALUES (4, 'POL101', 'Страхование жизни', '2023-04-01', '2024-04-01')")
    cursor.execute("INSERT INTO policies (client_id, policy_number, policy_type, start_date, end_date) VALUES (5, 'POL102', 'Страхование путешествий', '2023-05-01', '2024-05-01')")

    # Вставка заявлений
    cursor.execute("INSERT INTO claims (policy_id, claim_date, amount, status) VALUES (1, '2023-03-01', 10000, 'Ожидает обработки')")
    cursor.execute("INSERT INTO claims (policy_id, claim_date, amount, status) VALUES (2, '2023-04-01', 5000, 'Одобрено')")
    cursor.execute("INSERT INTO claims (policy_id, claim_date, amount, status) VALUES (3, '2023-05-01', 15000, 'Ожидает обработки')")
    cursor.execute("INSERT INTO claims (policy_id, claim_date, amount, status) VALUES (4, '2023-06-01', 20000, 'Одобрено')")
    cursor.execute("INSERT INTO claims (policy_id, claim_date, amount, status) VALUES (5, '2023-07-01', 25000, 'Ожидает обработки')")

    conn.commit()
    conn.close()

insert_data()