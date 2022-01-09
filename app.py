from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return "Flask application is running and created by Suraj"

if __name__=="__main__":
	app.run()