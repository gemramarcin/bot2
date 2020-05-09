from scapy.all import *
from scapy.layers.inet import IP, ICMP, TCP

targetip = '192.168.227.130'
closed_ports = []
open_ports = []


def is_up(ip):  # sprawdzanie czy host jest up za pomocą pinga (ICMP)
    ping = IP(dst=ip) /ICMP()
    response = sr(ping, timeout=3)
    if response == None:
        return False
    else:
        return True

# SKANOWANIE PÓŁOTWARTE
def main_function():
    ports = range(1, 3000)  # porty które chcemy przeskanować
    conf.verb=0 # wyłączenie verbose żeby nie wyświetlało zbednych rzeczy
    if is_up(targetip):
        print('Ping went well, start scanning ports of target...')
        for port in ports:
            print('Port ', port)
            source_port = RandNum(1024, 65535)
            packet = IP(dst=targetip) / TCP(sport=source_port, dport=port, flags='S')  # tworzenie pakietu SYN
            response = sr1(packet, timeout=3)
            if response == "<type 'NoneType'>":
                closed_ports.append(port)
            elif response.haslayer(TCP):

                if response.getlayer(TCP).flags == 0x12:  # jeżeli odpowiedzią jest SYN/ACK
                    open_ports.append(port)
                    rst = IP(dst=targetip) / TCP(sport=source_port, dport=port, flags='AR')  # tworzenie pakietu RST
                    sr(rst, timeout=3)
                elif response.getlayer(TCP).flags == 0x14:  # jeżeli odpowiedź to RST/ACK
                    closed_ports.append(port)

    print('Scanning done...')
    return 'Opened ports: ', open_ports
