# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import Flask, render_template, request, jsonify, abort
import jinja2
import sys
import os
import base64


from algorithm import correct
from algorithm import VSM
from algorithm import BS


vsm = VSM.VSM(21576)
bs = BS.boolsearch()
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')

@app.route('/api/correct', methods = ['GET'])
def correctwords():
    words = request.args.get('words')
    if words is not None:
        result = correct.correct(words)
        res = {}
        if (words == result):
            res['status'] = 0
        else:
            res['status'] = 1
        res['res'] = result
        return jsonify(res)
    else:
        abort(400)

def __search(query, K):
    flag = False     # 0 is bs
    for logical in bs.logical_words:
        if query.find(logical) > -1:
            flag = True
            break

    if flag:
        return bs.search(query, K)
    else:
        return vsm.search(query, K)

@app.route('/api/correctsearch', methods = ['GET'])
def correctSearch():
    original = request.args.get('words')
    K = int(request.args.get('k'))
    words = base64.b64decode(original).split(' ')
    status = 0                                      # status = 1 means that the words has has some errors

    query = []
    for word in words:
        if word is not None:
            if word not in bs.logical_words:
                result = correct.correct(word)
                if (word != result):
                    status = 1
                query.append(result)
            else:
                query.append(word)

    query = ' '.join(query)
    result = __search(query, K)
    res = {}
    res["status"] = status
    res["query"] = query
    res["result"] = result
    res["original"] = original
    return jsonify(res)

@app.route('/api/search', methods = ['GET'])
def searchwords():
    words = request.args.get('words')
    query = base64.b64decode(words)
    K = int(request.args.get('k'))
    result = __search(query, K)
    res = {}
    res["result"] = result
    return jsonify(res)

if __name__ == "__main__":
    print vsm.search("query", 100)

