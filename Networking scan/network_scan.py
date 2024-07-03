import socket
from scapy.all import ARP, Ether, srp

def get_ip_list():
    target_ip = "192.168.0.1/24"  # Adjust to your network's IP range
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send ARP request and capture responses
    result = srp(packet, timeout=6, retry=4, verbose=0)[0]  # Increased timeout and retries

    devices = []
    for sent, received in result:
        if received.haslayer('ARP'):
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def get_device_name(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.timeout):
        return None

def main():
    devices = get_ip_list()
    print(f"{'IP Address':<20}{'MAC Address':<20}{'Device Name':<20}")
    print("="*60)
    for device in devices:
        device_name = get_device_name(device['ip'])
        print(f"{device['ip']:<20}{device['mac']:<20}{device_name if device_name else 'Unknown':<20}")

if __name__ == "__main__":
    main()
