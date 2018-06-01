from flask import Flask, Response
from module.user import user

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return '<html><title>首页</title><body><p>welcome首页</p></body></html>'

app.register_blueprint(user, url_prefix='/user')

if __name__ == '__main__':
    app.run()
