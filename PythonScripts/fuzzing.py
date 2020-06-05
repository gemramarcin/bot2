from scapy.all import *
from scapy.layers.http import HTTP
from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.l2 import Ether, ARP
from scapy.layers.ntp import NTP


def main_function(targetip,numberOfPackets):
    for i in range(1,int(numberOfPackets)):
         sr1(IP(dst=targetip) / fuzz(TCP(dport=80) / NTP(version=4)), timeout=0) # wysyłanie spoofingu domyślnie na port 80
    return 'Fuzzing done'