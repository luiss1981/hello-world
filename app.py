from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/nosotros')
def nosotros():
    return jsonify('Estamos en nosotros !!!')



if __name__ == '__main__':
    app.run(debug=True)