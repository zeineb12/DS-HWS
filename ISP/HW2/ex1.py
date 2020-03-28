#Relavant imports
from flask import Flask
from flask import request
from flask import abort
import base64

app = Flask(__name__)

@app.route('/hw2/ex1', methods=['POST'])

#Login function and returned request
def login():
    data= request.get_json()

    mySecureOneTimePad = "Never send a human to do a machine's job";
    username= data["user"]
    password= data["pass"]
    encry_username= superEncryption(username,mySecureOneTimePad)
    if encry_username==password:
        return "200"
    else: abort(400)

#SuperEncryption method translated into python code
def superEncryption(msg, key):

    if (len(key) < len(msg)):
        diff = len(msg) - len(key)
        key = key + key[:diff]
      
    l1 = list(msg)
    l2 = list(key[:len(msg)])
   
    l1=map (lambda x: ord(x), l1)
    l2=map (lambda x: ord(x), l2)
    l1= map (lambda x,y : (chr(x ^ y)) , l1, l2)
    res = ''.join(l1)

    return base64.b64encode(bytes(res, 'utf-8')).decode('utf-8')

#Running the Flask app
if __name__ == "__main__":
    app.run()