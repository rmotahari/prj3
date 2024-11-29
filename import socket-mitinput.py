import socket
import logging

def get_ip_addresses(server_names):
    ip_addresses = {}
    logging.basicConfig(filename='ip_lookup.log', level=logging.DEBUG)
    
    for server in server_names:
        server = server.strip()  # Entfernt führende und nachfolgende Leerzeichen
        try:
            ip = socket.gethostbyname(server)
            if ip.startswith('10.60.'):
                location = 'Buero'
            elif ip.startswith('10.10.'):
                location = 'Home Office'
            else:
                location = 'Unbekannt'
            ip_addresses[server] = f"{ip} ({location})"
        except socket.gaierror as err:
            logging.error(f"Error resolving {server}: {err}")
            ip_addresses[server] = f"Error: {err}"
        except Exception as err:
            logging.error(f"Unexpected error with {server}: {err}")
            ip_addresses[server] = f"Error: {err}"
    
    return ip_addresses

def write_ip_addresses_to_file(ip_addresses, output_file):
    try:
        with open(output_file, 'w') as file:
            for server, ip in ip_addresses.items():
                file.write(f"{server}: {ip}\n")
    except IOError as e:
        logging.error(f"An I/O error occurred: {e}")
        return f"Ein Fehler ist aufgetreten: {e}"
    
    logging.info("IP addresses successfully exported.")
    return "IP-Adressen erfolgreich exportiert."

# Beispiel-Verwendung
server_names = [
'CMP15873',
'CMP15874',
'CMP09063',
'CMP09203',
'CMP08278']
output_file = r'C:\Devops\ip_addresses.txt'
ip_addresses = get_ip_addresses(server_names)
result = write_ip_addresses_to_file(ip_addresses, output_file)
print(result)