# Put your app in here.
from flask import Flask, request
from operations import add,sub,mult,div
app = Flask(__name__)

math_operations = {
    "add" : add,
    "sub" : sub,
    "mult" : mult,
    "div" : div
}

#not sure if this wasnt working because i had int:a and int: b inside path /math/<mathfunc>


@app.route('/math/<mathfunc>')
def math_funcs(mathfunc):
    a = int(request.args.get('a',0))
    b = int(request.args.get('b',0))
    math_op = math_operations.get(mathfunc)
    outcome = math_op(a,b) if math_op else None
    return str(outcome) #f"<h1>your answer to the math problem is {outcome}</h1>" if outcome is not None else f"<h1>invalid</h1>"



