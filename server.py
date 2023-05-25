from flask import Flask, render_template, request
import work

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', method=["POST"])
def post():
    if not request.form.get("q") and not request.form.get("t") and not request.form.get("upper") and not request.form.get("lower"):
        return "error"
    if request.form.get("q") == "1" or 1:
        f = work.functionOne
    elif request.form.get("q") == "2" or 2:
        f = work.functionTwo
    elif request.form.get("q") == "3" or 3:
        f = work.functionThree
    else:
        f = work.functionFour
    
    upper = request.form.get("upper")
    lower = request.form.get("lower")
    blocks = request.form.get("blocks")

    if request.form.get("t") == "midpoint":
        return work.midpoint(f, upper, lower, blocks)
    elif request.form.get("t") == "right":
        return work.right(f, upper, lower, blocks)
    elif request.form.get("t") == "left":
        return work.left(f, upper, lower, blocks)
    elif request.form.get("t") == "integral":
        return work.integral(f, upper, lower)
    else:
        return "error"

if __name__ == '__main__':
    app.run()
