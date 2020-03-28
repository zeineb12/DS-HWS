from flask import Flask, request, json
import bcrypt

app = Flask(__name__)
@app.route('/hw4/ex2', methods=['POST'])

def login():
    username=request.json['user']
    password = request.json['pass']
    encoded_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(encoded_password,salt)
    return password_hash, 200
app.run()
