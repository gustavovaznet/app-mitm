from scapy.all import *

# PRINT PACKET
def print_packet(pkt):
    data_packet = raw(pkt[TCP].payload).decode("latin-1")
    print(data_packet)


packet = sniff(filter="tcp", prn=print_packet, store=0)
