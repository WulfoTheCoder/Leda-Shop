from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import random
import string
import requests
from datetime import date

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    r = ''
    r += render_template('essentials/header.html')
    r += render_template('index.html')
    r += render_template('essentials/footer.html', now=date.today().year)
    return r

@app.route('/about/')
def about():
    r = ''
    r += render_template('essentials/header.html')
    r += render_template('about.html')
    r += render_template('essentials/footer.html', now=date.today().year)
    return r

if __name__ == '__main__':
    app.run(debug=True)