# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import Flask, render_template, request, jsonify, abort
import jinja2
import sys
import os
import base64

from algorithm import VSM
from algorithm import correct

vsm = VSM.VSM(100)
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')

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

@app.route('/api/correctsearch', methods = ['GET'])
def correctSearch():
    words = request.args.get('words')
    words = base64.b64decode(words).split(' ')
    print words
    status = 0       # status = 1 means that the words has has some errors

    query = []
    for word in words:
        if word is not None:
            result = correct.correct(word)
            if (word != result):
                status = 1
            query.append(result)

    query = ' '.join(query)
    result = vsm.search(query, 100)
    res = {}
    res["status"] = status
    res["query"] = query
    res["result"] = result
    return jsonify(res)

@app.route('/api/search', methods = ['GET'])
def searchwords():
    word = request.args.get('word')
    if word is not None:
        result = vsm.search(word, 100)
        res = {}
        res["result"] = result
        return jsonify(res)
    else:
        abort(400)
