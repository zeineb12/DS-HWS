#!/usr/bin/env python3
import os
import sys
import populate
from flask import g
from flask import Flask, current_app
from flask import render_template, request, jsonify
import pymysql


app = Flask(__name__)
username = "root"
password = "root"
database = "hw4_ex3"

## This method returns a list of messages in a json format such as 
## [
##  { "name": <name>, "message": <message> },
##  { "name": <name>, "message": <message> },
##  ...
## ]
## If this is a POST request and there is a parameter "name" given, then only
## messages of the given name should be returned.
## If the POST parameter is invalid, then the response code must be 500.
@app.route("/messages",methods=["GET","POST"])
def messages():
    with db.cursor() as cursor:
        ## your code here 
        name=""
        method= request.method
        if (method == "POST"):
             name=request.values.get("name")
             if name is None :
                  abort(500)
             else:
                  cursor.execute('select * from messages where name like %s', name)
        else : 
             cursor.execute('select * from messages')
        json=list()
        iterator = cursor.fetchall()
        for i in iterator :
             json.append({"name": i[0], "message": i[1]})
        return jsonify(json),200


## This method returns the list of users in a json format such as
## { "users": [ <user1>, <user2>, ... ] }
## This methods should limit the number of users if a GET URL parameter is given
## named limit. For example, /users?limit=4 should only return the first four
## users.
## If the paramer given is invalid, then the response code must be 500.
@app.route("/users",methods=["GET"])
def contact():
    with db.cursor() as cursor:
        ## your code here 
        nbr_users=request.args.get('limit')
        if nbr_users != None:
             nbr_users=nbr_users.split("'")
        if nbr_users != None:
             if len(nbr_users) !=1:
                  abort(500)
             else:
                  cursor.execute('select name from users limit %s', int(nbr_users[0]))
        else:
             cursor.execute('select name from users')
     
        json=list()
        row = cursor.fetchall()
        for i in row :
             json.append( i[0])
        return jsonify({"users": json}),200

if __name__ == "__main__":
    seed = "randomseed"
    if len(sys.argv) == 2:
        seed = sys.argv[1]

    db = pymysql.connect("localhost",
                username,
                password,
                database)
    with db.cursor() as cursor:
        populate.populate_db(seed,cursor)             
        db.commit()
    print("[+] database populated")

    app.run(host='0.0.0.0',port=80)