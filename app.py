from flask import Flask
# from 'Database/events.py' import events

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/<name>')
def index():
    return "Hi "


if __name__ == '__main__':
    app.run()