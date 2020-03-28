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
	payload = {'product': 'r2lGqwworIIIGeVDv0riNI/pqb7XcCRMlPPEw+7xDXc=', 'shipping_address': 'zeineb.sahnoun@epfl.ch'}
	headers = {'content-type': 'application/json', 'Content-Length': '91', 'User-Agent': 'Dumb Generator', 'Host': 'com402.epfl.ch'}
	r = requests.post('http://com402.epfl.ch/hw1/ex3/shipping', json=payload, headers=headers)
	print("status    " , r.status_code,"  text  ", r.text)
	print('')

nfqueue.unbind()
