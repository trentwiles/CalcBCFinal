from flask import Flask, render_template, request, send_from_directory
import work

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/static/<path:path>')
def stat(path):
    return send_from_directory('static', path)

@app.route('/', methods=["POST"])
def post():
    if not request.form.get("q") and not request.form.get("t") and not request.form.get("upper") and not request.form.get("lower"):
        return "error"
    if request.form.get("q") == "1" or request.form.get("q") == 1:
        f = work.functionOne
    elif request.form.get("q") == "2" or request.form.get("q") == 2:
        f = work.functionTwo
    elif request.form.get("q") == "3" or request.form.get("q") == 3:
        f = work.functionThree
    else:
        f = work.functionFour
    
    upper = float(request.form.get("upper"))
    lower = float(request.form.get("lower"))
    blocks = int(request.form.get("blocks"))

    if request.form.get("t") == "midpoint":
        return str(work.midpoint(f, float(upper), lower, blocks))
    elif request.form.get("t") == "right":
        return str(work.right(f, upper, lower, blocks))
    elif request.form.get("t") == "left":
        return str(work.left(f, upper, lower, blocks))
    elif request.form.get("t") == "integral":
        return str(work.integral(f, upper, lower))
    else:
        return "error"

if __name__ == '__main__':
    app.run()
