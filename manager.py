# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import Flask, render_template
import jinja2

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')
