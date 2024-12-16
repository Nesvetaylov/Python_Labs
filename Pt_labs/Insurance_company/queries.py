# Содержит функции для выполнения статистических запросов
import sqlite3  

# Получает список клиентов и количество полисов, которые у них есть
def select_clients_with_policies(conn):
    query = """
    SELECT c.Name, COUNT(p.PolicyID) AS PolicyCount
    FROM Clients c
    LEFT JOIN Policies p ON c.ClientID = p.ClientID
    GROUP BY c.ClientID;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Получает сводку по заявкам (claims) для каждого полиса
def select_claims_summary(conn):
    query = """
    SELECT p.PolicyID, COUNT(c.ClaimID) AS ClaimCount
    FROM Policies p
    LEFT JOIN Claims c ON p.PolicyID = c.PolicyID
    GROUP BY p.PolicyID;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Получает общую сумму всех заявок
def select_total_claims_amount(conn):
    query = """
    SELECT SUM(Amount) AS TotalClaimsAmount
    FROM Claims;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()