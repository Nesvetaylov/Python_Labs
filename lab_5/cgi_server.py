import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import json
from lxml import etree

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('''
                <html>
                <body>
                    <h1>Форма добавления клиента, полиса и заявления</h1>
                    <form method="POST" action="/add_client">
                        Имя: <input type="text" name="name" required><br>
                        Email: <input type="text" name="email" required><br>
                        Номер полиса: <input type="text" name="policy_number" required><br>
                        Тип полиса: <input type="text" name="policy_type" required><br>
                        Дата начала: <input type="date" name="start_date" required><br>
                        Дата окончания: <input type="date" name="end_date" required><br>
                        Дата заявления: <input type="date" name="claim_date" required><br>
                        Сумма: <input type="number" name="amount" required><br>
                        Статус: <input type="text" name="status" required><br>
                        <input type="submit" value="Добавить клиента, полис и заявление">
                    </form>
                    <br>
                    <a href="/view_clients">Посмотреть список клиентов</a>
                    <br>
                    <a href="/save_clients_json">Сохранить клиентов в JSON</a>
                    <br>
                    <a href="/save_clients_xml">Сохранить клиентов в XML</a>
                </body>
                </html>
            '''.encode('utf-8'))
        elif self.path == '/view_clients':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            html = self.display_data()
            self.wfile.write(html.encode('utf-8'))#отправляем полученный html-код клиенту

        elif self.path == '/save_clients_json':
            self.save_all_to_json()
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('Данные успешно сохранены в clients.json'.encode('utf-8'))
        elif self.path == '/save_clients_xml':
            self.save_all_to_xml()
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('Данные успешно сохранены в clients.xml'.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            error_message = '404 - Страница не найдена'
            self.wfile.write(error_message.encode('utf-8'))

    def display_data(self):
        conn = sqlite3.connect('insurance_company.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()

        cursor.execute("SELECT * FROM policies")
        policies = cursor.fetchall()

        cursor.execute("SELECT * FROM claims")
        claims = cursor.fetchall()

        conn.close()

        html = '<html><body>'
        html += '<h1>Клиенты</h1><table border="1"><tr><th>ID</th><th>Имя</th><th>Email</th></tr>'
        for client in clients:
            html += f'<tr><td>{client[0]}</td><td>{client[1]}</td><td>{client[2]}</td></tr>'
        html += '</table>'

        html += '<h1>Полисы</h1><table border="1"><tr><th>ID</th><th>Клиент ID</th><th>Номер полиса</th><th>Тип полиса</th><th>Дата начала</th><th>Дата окончания</th></tr>'
        for policy in policies:
            html += f'<tr><td>{policy[0]}</td><td>{policy[1]}</ td><td>{policy[2]}</td><td>{policy[3]}</td><td>{policy[4]}</td><td>{policy[5]}</td></tr>'
        html += '</table>'

        html += '<h1>Заявления</h1><table border="1"><tr><th>ID</th><th>Полис ID</th><th>Дата заявления</th><th>Сумма</th><th>Статус</th></tr>'
        for claim in claims:
            html += f'<tr><td>{claim[0]}</td><td>{claim[1]}</td><td>{claim[2]}</td><td>{claim[3]}</td><td>{claim[4]}</td></tr>'
        html += '</table>'

        html += '</body></html>'
        return html

    def save_all_to_json(self):
        conn = sqlite3.connect('insurance_company.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()

        cursor.execute("SELECT * FROM policies")
        policies = cursor.fetchall()

        cursor.execute("SELECT * FROM claims")
        claims = cursor.fetchall()

        conn.close()

        data = {
            "clients": [{"id": client[0], "name": client[1], "email": client[2]} for client in clients],
            "policies": [{"id": policy[0], "client_id": policy[1], "policy_number": policy[2], "policy_type": policy[3], "start_date": policy[4], "end_date": policy[5]} for policy in policies],
            "claims": [{"id": claim[0], "policy_id": claim[1], "claim_date": claim[2], "amount": claim[3], "status": claim[4]} for claim in claims]
        }

        with open('clients.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def save_all_to_xml(self):
        conn = sqlite3.connect('insurance_company.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()

        cursor.execute("SELECT * FROM policies")
        policies = cursor.fetchall()

        cursor.execute("SELECT * FROM claims")
        claims = cursor.fetchall()

        conn.close()

        root = etree.Element("data")

        clients_element = etree.SubElement(root, "clients")
        for client in clients:
            client_element = etree.SubElement(clients_element, "client")
            etree.SubElement(client_element, "id").text = str(client[0])
            etree.SubElement(client_element, "name").text = client[1]
            etree.SubElement(client_element, "email").text = client[2]

        policies_element = etree.SubElement(root, "policies")
        for policy in policies:
            policy_element = etree.SubElement(policies_element, "policy")
            etree.SubElement(policy_element, "id").text = str(policy[0])
            etree.SubElement(policy_element, "client_id").text = str(policy[1])
            etree.SubElement(policy_element, "policy_number").text = policy[2]
            etree.SubElement(policy_element, "policy_type").text = policy[3]
            etree.SubElement(policy_element, "start_date").text = policy[4]
            etree.SubElement(policy_element, "end_date").text = policy[5]

        claims_element = etree.SubElement(root, "claims")
        for claim in claims:
            claim_element = etree.SubElement(claims_element, "claim")
            etree.SubElement(claim_element, "id").text = str(claim[0])
            etree.SubElement(claim_element, "policy_id").text = str(claim[1])
            etree.SubElement(claim_element, "claim_date").text = claim[2]
            etree.SubElement(claim_element, "amount").text = str(claim[3])
            etree.SubElement(claim_element, "status").text = claim[4]

        xml_str = etree.tostring(root, pretty_print=True, encoding='utf-8').decode('utf-8')

        with open('clients.xml', 'w', encoding='utf-8') as xml_file:
            xml_file.write(xml_str)

    def do_POST(self):
        if self.path == '/add_client':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            parsed_data = urlparse.parse_qs(post_data.decode('utf-8'))

            name = parsed_data.get('name', [None])[0]
            email = parsed_data.get('email', [None])[0]
            policy_number = parsed_data.get('policy_number', [None])[0]
            policy_type = parsed_data.get('policy_type', [None])[0]
            start_date = parsed_data.get('start_date', [None])[0]
            end_date = parsed_data.get('end_date', [None])[0]
            claim_date = parsed_data.get('claim_date', [None])[0]
            amount = parsed_data.get('amount', [None])[0]
            status = parsed_data.get('status', [None])[0]

            if name and email and policy_number and policy_type and start_date and end_date and claim_date and amount and status:
                try:
                    client_id = self.insert_client(name, email)
                    policy_id = self.insert_policy(client_id, policy_number, policy_type, start_date, end_date)
                    self.insert_claim(policy_id, claim_date, amount, status)

                    self.send_response(302)
                    self.send_header('Location', '/view_clients')
                    self.end_headers()
                except sqlite3.IntegrityError as e:
                    self.send_response(400)
                    self.send_header('Content-type', 'text/html; charset=utf-8')
                    self.end_headers()
                    error_message = f'Ошибка: {str(e)}'
                    self.wfile.write(error_message.encode('utf-8'))
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                error_message = 'Ошибка: все поля обязательны.'
                self.wfile.write(error_message.encode('utf-8'))

    def insert_claim(self, policy_id, claim_date, amount, status):
        conn = sqlite3.connect('insurance_company.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO claims (policy_id, claim_date, amount, status) VALUES (?, ?, ?, ?)",
                       (policy_id, claim_date, amount, status))
        conn.commit()
        conn.close()

    def insert_client(self, name, email):
        conn = sqlite3.connect('insurance_company.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        client_id = cursor.lastrowid
        conn.close()
        return client_id

    def insert_policy(self, client_id, policy_number, policy_type, start_date, end_date):
        conn = sqlite3.connect('insurance_company.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO policies (client_id, policy_number, policy_type, start_date, end_date) VALUES (?, ?, ?, ?, ?)",
            (client_id, policy_number, policy_type, start_date, end_date))
        conn.commit()
        policy_id = cursor.lastrowid
        conn.close()
        return policy_id

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting CGI server on port {port}...')
    httpd.serve_forever()

run()