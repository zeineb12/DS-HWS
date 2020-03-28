#relevant imports
from flask import Flask, request, abort, make_response
import base64
import hmac
import hashlib
import time

app = Flask(__name__)


@app.route('/ex3/login', methods=['POST'])
#login function and sent cookie
def login():
    data = request.get_json()
    timestamp = int(time.time())

    if (data["user"] == "administrator" and data["pass"] == "42"):
        str_cookie = "administrator" + "," + str(timestamp) + ",com402,hw2,ex3,administrator"
        cookie = str_cookie + "," + hmac.new(b'NAAfCxdCXRYPDE4OVQY1CBEITFoMSA==', str_cookie.encode('utf-8'), hashlib.sha256).hexdigest() 
        r= make_response()
        r.set_cookie("LoginCookie", base64.b64encode(cookie.encode('utf-8')))
        return r , 200
    else:
        str_cookie = data["user"] + "," + str(timestamp) + ",com402,hw2,ex3,user"
        cookie = str_cookie + "," + hmac.new(b'NAAfCxdCXRYPDE4OVQY1CBEITFoMSA==', str_cookie.encode('utf-8') , hashlib.sha256).hexdigest() 
        r=make_response()
        r.set_cookie("LoginCookie", base64.b64encode(cookie.encode('utf-8')))
        return r , 200
    
    

@app.route('/ex3/list', methods=['POST', 'GET'])
#POST request and cookie verification
def list():
    get_cookie = (base64.b64decode(request.cookies.get('LoginCookie')).decode('utf-8')).split(',')
    get_h = get_cookie.pop()
    true_h = hmac.new(b'NAAfCxdCXRYPDE4OVQY1CBEITFoMSA==', (','.join(get_cookie)).encode('utf-8'), hashlib.sha256).hexdigest()
    cookie = (','.join(get_cookie)).split(',')
    if(true_h == get_h):
    	if (cookie[0] == "administrator"):
    		return "Admin", 200
    	else:
    		return "User", 201
    else:
    	abort(403)

if __name__ == "__main__":
    app.run()