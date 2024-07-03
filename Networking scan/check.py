import socket
import netifaces

def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # Get default gateway and interface information
    gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
    interface = netifaces.gateways()['default'][netifaces.AF_INET][1]

    # Get interface IP addresses
    addresses = netifaces.ifaddresses(interface)
    ipv4 = addresses[netifaces.AF_INET][0]['addr']
    netmask = addresses[netifaces.AF_INET][0]['netmask']

    return {
        'hostname': hostname,
        'ip_address': ip_address,
        'gateway': gateway,
        'interface': interface,
        'ipv4': ipv4,
        'netmask': netmask
    }

# Example usage:
network_info = get_network_info()
print("Network Information:")
print(f"Hostname: {network_info['hostname']}")
print(f"IP Address: {network_info['ip_address']}")
print(f"Default Gateway: {network_info['gateway']}")
print(f"Interface: {network_info['interface']}")
print(f"Interface IPv4 Address: {network_info['ipv4']}")
print(f"Netmask: {network_info['netmask']}")
