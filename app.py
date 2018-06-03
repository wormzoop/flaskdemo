from flask import Flask, session
from module.user import user
from module.mall import mall
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jiji78978uihuih877'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

@app.route('/', methods=['GET','POST'])
def home():
    return '<html><title>首页</title><body><p>welcome首页</p></body></html>'

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(mall, url_prefix='/mall')

if __name__ == '__main__':
    app.run()
