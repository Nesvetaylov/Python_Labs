import json
import xml.etree.ElementTree as ET

def export_to_json(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    with open('clients.json', 'w') as json_file:
        json.dump(clients, json_file)

def export_to_xml(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()

    root = ET.Element("clients")
    for client in clients:
        client_elem = ET.SubElement(root, "client")
        ET.SubElement(client_elem, "id").text = str(client[0])
        ET.SubElement(client_elem, "name").text = client[1]
        ET.SubElement(client_elem, "email").text = client[2]

    tree = ET.ElementTree(root)
    tree.write("clients.xml")