from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return '<html><title>首页</title><body><p>welcome首页</p></body></html>'

@app.route('/user/list', methods=['GET'])
def userlist():
    

if __name__ == '__main__':
    app.run()
