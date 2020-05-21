from scapy.all import *
from scapy.layers.http import HTTP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether, ARP
from scapy.layers.ntp import NTP


def main_function(targetip,numberOfPackets):
    # packets=[]
    for i in range(1,numberOfPackets):
         send(fuzz(IP(dst=targetip)))
    # return packets
    # send(IP(dst=targetip) / fuzz(UDP() / NTP(version=4)))
    # return targetip + " " + numberOfPackets