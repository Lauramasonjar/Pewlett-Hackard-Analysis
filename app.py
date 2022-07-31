# import dependencies
from flask import Flask

# creat a new flask instance call 'app'
app = Flask(__name__)

# define the starting point (root)
# create a function called hello_world
@app.route('/')
def hello_world():
    return 'Hello world'

    # run a flask app
    # export FLASK_APP=app.py