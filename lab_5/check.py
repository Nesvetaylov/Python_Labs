import sqlite3
def check_clients():
    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()

    print("Список клиентов:")
    for client in clients:
        print(f"ID: {client[0]}, Имя: {client[1]}, Email: {client[2]}")

    conn.close()

def check_policies():
    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM policies")
    policies = cursor.fetchall()

    print("\nСписок полисов:")
    for policy in policies:
        print(f"ID: {policy[0]}, Клиент ID: {policy[1]}, Номер полиса: {policy[2]}, Тип полиса: {policy[3]}, Дата начала: {policy[4]}, Дата окончания: {policy[5]}")

    conn.close()

def check_claims():
    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM claims")
    claims = cursor.fetchall()

    print("\nСписок заявлений:")
    for claim in claims:
        print(f"ID: {claim[0]}, Полис ID: {claim[1]}, Дата заявления: {claim[2]}, Сумма: {claim[3]}, Статус: {claim[4]}")

    conn.close()


check_clients()
check_policies()
check_claims()