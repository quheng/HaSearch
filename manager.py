# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import Flask, render_template, request, jsonify, abort
import jinja2
import sys
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')

from algorithm import correct
@app.route('/api/correct', methods = ['GET'])
def correctwords():
    word = request.args.get('word')
    if word is not None:
        result = correct.correct(word)
        res = {}
        if (word == result):
            res['status'] = 0
        else:
            res['status'] = 1
        res['res'] = result
        return jsonify(res)
    else:
        abort(400)
