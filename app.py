from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method=='POST':
        email = request.form["email_name"]
        password = request.form["email_password"]
        print('Printing email and password from the application :- {0} {1}'.format(email, password))
        return render_template("in.html")

@app.route("/up", methods=["GET", "POST"])
def up():
    return render_template("up.html")

@app.route("/fp", methods=["GET", "POST"])
def fp():
    return render_template("up.html")


if __name__ == '__main__':
    app.debug =True
    app.run()