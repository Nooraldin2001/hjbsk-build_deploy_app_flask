from flask import Flask, render_template, request
from Maths.mathematics import summation,subraction,multipliacation
# Import the Maths package here

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = summation(num1, num2)
        return str(result)
    except(ValueError, TypeError):
        return "Invalid input. Please provide numeric values for 'num1' and 'num2.", 400
    # Write your code here

@app.route("/sub")
def sub_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = subraction(num1, num2)
        return str(result)
    except(ValueError, TypeError):
        return "Invalid input. Please provide numeric values for 'num1' and 'num2.", 400
    # Write your code here

@app.route("/mul")
def mul_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = multipliacation(num1, num2)
        return str(result)
    except(TypeError, ValueError):
        return "Invalid input. Please provide numeric values for 'num1' and 'num2.", 400
    # Write your code here  

@app.route("/")
def render_index_page():
    # Write your code here
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
