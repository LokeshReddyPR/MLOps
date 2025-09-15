from flask import Flask

app = Flask(__name__)  # Creates an instance of flask class which will be you WSGI


@app.route("/")
def Welcome():
    return "Welcome to the Flask COurse. THis should be a amazing course"


@app.route("/index")
def index():
    return "Welcome to the Flask COurse. THis should be a Index page"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
