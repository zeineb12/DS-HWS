from netfilterqueue import NetfilterQueue
from scapy.all import *
import json
import requests


def callback(pkt):
    print(pkt)
    ip = IP(pkt.get_payload())
    if ip.haslayer(Raw):
        tcp_payload = ip["Raw"].load
        if tcp_payload[0] == 0x16 and tcp_payload[1] == 0x03 and tcp_payload[2] == 0x01 and tcp_payload[5] == 0x01 and tcp_payload[9] == 0x03 and (tcp_payload[10] == 0x03 or tcp_payload[10] == 0x02):
            pkt.drop()
            new_packet = IP(dst=ip.dst, src="172.16.0.3") / TCP()
            new_packet[TCP].sport = ip[TCP].sport
            new_packet[TCP].dport = ip[TCP].dport
            new_packet[TCP].seq = ip[TCP].seq
            new_packet[TCP].ack = ip[TCP].ack
            new_packet[TCP].flags = 'FA'
            send(new_packet)
        else:
            pkt.accept()
    else:
        pkt.accept()


nfqueue = NetfilterQueue()
nfqueue.bind(0, callback, 100)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()
