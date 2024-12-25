import sqlite3
def statistical_queries():
    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()

    # 1. Количество клиентов
    cursor.execute("SELECT COUNT(*) FROM clients")
    print("Количество клиентов:", cursor.fetchone()[0])

    # 2. Общее количество полисов
    cursor.execute("SELECT COUNT(*) FROM policies")
    print("Общее количество полисов:", cursor.fetchone()[0])

    # 3. Сумма всех заявленных сумм
    cursor.execute("SELECT SUM(amount) FROM claims")
    print("Сумма всех заявленных сумм:", cursor.fetchone()[0])

    conn.close()

statistical_queries()