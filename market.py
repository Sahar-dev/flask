from flask import Flask, render_template
# initialisation built in var refer to local python file
app = Flask(__name__)

# decorator : one step a function before excuted ,
# root url

# set FLASK_APP=market.py
# http://127.0.0.1:5000/
# set FLASK_DEBUG=1


# @app.route('/')
# def hello_world():
#   return '<h1>hello world with debug<h1>'

# http://127.0.0.1:5000/about

# @app.route('/about')
# def about_page():
# return '<h1>this is the abt page of </h1>'

# http://127.0.0.1:5000/about/sahar
# <username> accept any var there


# @app.route('/about/<username>')
# def about_page(username):
# return f'<h1>this is the abt page of {username}</h1>'

# we create templates and refer our routes to those diff htmls


@app.route('/')
def home_page():
    return render_template('home.html')
# py -m venv .env
# .env\scripts\activate
# pip install -r req.txt
