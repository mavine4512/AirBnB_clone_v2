#!/usr/bin/python3
"""Write script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


def format_text(text):
    """rep underscores with space"""
    return text.replace("_", " ")



@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return ("Hello HBNB!")


@app.route('/hbnb/', strict_slashes=False)
def hbnb():
    """Return a given string"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """Display C followed by the value of the text variable"""
    return "C {}".format(format_text(text))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_Text(text="is cool"):
    """Display Python follow by the valus of the text variable"""
    return "Python {}".format(format_text(text))


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    """display "n is number" only if n is a integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
