# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 10:09:24 2022

@author: user
"""
from flask import Flask, render_template, jsonify
import pandas as pd
from six.moves import urllib
import json
from myAPI import index2

app = Flask(__name__)

@app.route("/iii")
def index():
    return render_template('index.html')
 
@app.route("/")
def index2():
    return  index2()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)