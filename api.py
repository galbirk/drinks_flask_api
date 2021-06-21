from flask import Flask , jsonify
import pymongo


app = Flask(__name__)


@app.route('/')
def index():
    return 'hello222!'

@app.route('/drinks')
def get_drinks():
    return jsonify({ 'text': 'drinks' })


if __name__ == "__main__":
    app.run(debug=True)
