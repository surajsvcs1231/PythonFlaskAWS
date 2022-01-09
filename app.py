from flask import Flask

app1 = Flask(__name__)

def get():
    return {'message':"Hello Suraj"}

app1.run(port = 5000)