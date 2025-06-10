from scapy.all import *

# HOST
hosts = ["bing.com"]

# PACKET
packet = IP(dst=hosts)/TCP(dport=(1,500), flags="S")
responded, not_responded = sr(packet, timeout=1)

# RESPONSE
for n in range(len(responded)):
    print("{} -> {}".format(responded[n][0][IP].dst, responded[n][0][TCP].dport))
