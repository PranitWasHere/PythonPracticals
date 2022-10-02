from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f/<temp>')
def celcius_to_fahrenheit(temp=""):
    temp = float(temp)
    fahrenheit = temp * (9 / 5) + 32
    return f"<h1>{temp} °C = {fahrenheit} °F</h1>"


if __name__ == '