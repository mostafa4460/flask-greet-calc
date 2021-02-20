from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def get_add():
    " Adds and returns 2 numbers passed in the query string "

    (a, b) = (int(request.args.get("a")), int(request.args.get("b")))
    return f"{add(a, b)}"

@app.route('/sub')
def get_sub():
    " Subtracts and returns 2 numbers passed in the query string "

    (a, b) = (int(request.args.get("a")), int(request.args.get("b")))
    return f"{sub(a, b)}"

@app.route('/mult')
def get_mult():
    " Multiplies and returns 2 numbers passed in the query string "

    (a, b) = (int(request.args.get("a")), int(request.args.get("b")))
    return f"{mult(a, b)}"

@app.route('/div')
def get_div():
    " Divides and returns 2 numbers passed in the query string "

    (a, b) = (int(request.args.get("a")), int(request.args.get("b")))
    return f"{div(a, b)}"

OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def do_math(operation):
    """ Does different math operations based on url visited on 2 numbers passed into the query string (a & b)  """

    (a, b) = (int(request.args.get("a")), int(request.args.get("b")))
    return f"{OPERATIONS[operation](a, b)}"