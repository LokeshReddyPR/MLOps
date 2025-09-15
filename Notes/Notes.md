
Flask Framework :


Uses :

WSGI : Web Server Gateway Interface 


![alt text](image.png)


Jinja 2 Template Engine :
    Web Template Engine - combines pages ina website with a data source

![alt text](image-1.png)

    Example:
![alt text](image-2.png)


Basic skeleton for Flask:
from flask import Flask

app = Flask(__name__) #Creates an instance of Flask class which will be your WSGI application


if __name__ == "__main__":
    app.run()
