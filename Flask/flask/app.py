from flask import Flask

app = Flask(__name__) #Creates an instance of flask class which will be you WSGI



@app.route("/")
def Welcome():
    return("Welcome to the Flask COurse")


if __name__=="__main__":
    app.run()




