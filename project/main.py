from flask import Flask
app = Flask(__name__)
PORT = 5000
DEBUG = False

@app.errorhandler(404)
def not_found(error):
    return 'Not found'


@app.route('/', methods = ['GET'])
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)