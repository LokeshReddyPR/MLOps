from flask import Flask, render_template

app = Flask(__name__)  # Creates an instance of flask class which will be you WSGI


@app.route("/")
def Welcome():
    return "<html><H1>Welcome To This page </H1></html>"


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
