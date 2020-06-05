from scapy.all import *
from scapy.layers.inet import IP, ICMP, TCP



def is_up(ip):  # sprawdzanie czy host jest up za pomocą pinga (ICMP)
    ping = IP(dst=ip) /ICMP()
    response = sr1(ping, timeout=3)
    if response == None:
        return False
    else:
        return True

# TCP CONNECT
def main_function(targetip, portRange):
    open_ports = []
    closed_ports=[]
    ports = range(int(portRange[0]), int(portRange[1]))  # porty które chcemy przeskanować
    conf.verb=0 # wyłączenie verbose żeby nie wyświetlało zbednych rzeczy
    if is_up(targetip):
        print('Ping went well, start scanning ports of target...')
        for port in ports:
            print('Port ', port)
            source_port = RandNum(1024, 65535)
            packet = IP(dst=targetip) / TCP(sport=source_port, dport=port, flags='S')  # tworzenie pakietu SYN
            response = sr1(packet, timeout=3)
            if str(type(response)) == "<type 'NoneType'>":
                closed_ports.append(port)
            elif response is None:
                pass
            elif response.haslayer(TCP):
                if response.getlayer(TCP).flags == 0x12:  # jeżeli odpowiedzią jest SYN/ACK
                    open_ports.append(port)
                    rst = IP(dst=targetip) / TCP(sport=source_port, dport=port, flags=0x4)  # tworzenie pakietu RST
                    sr1(rst, timeout=0)
                elif response.getlayer(TCP).flags == 0x14:  # jeżeli odpowiedź to RST/ACK
                    closed_ports.append(port)
    else:
        return 'Host is not active'
    print(open_ports)
    return 'Opened ports: ', open_ports
