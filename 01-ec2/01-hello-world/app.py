from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World! This is my first App on AWS EC2!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)