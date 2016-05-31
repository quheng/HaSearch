# !/usr/bin/env python
# coding=utf8
# Author: quheng
import os
import cPickle
import re
import gzip

def build(path):
    postfix = re.compile(r"\.(\w+)$")
    name = re.compile(r"(\w+)\.\w+$")
    inverse_index = {}
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            post = postfix.findall(filename)[0]
            if post != 'html':
                continue
            filepath = dirpath + filename
            f = open(filepath, 'r')
            words = f.read().split(' ')
            index = {}
            for word in words:
                word = word.strip(' ,\n')
                if not word:
                    continue
                if word in index:
                    index[word] += 1
                else:
                    index[word] = 1
            for item in index:
                new_item = {}
                new_item["doc"] = name.findall(filename)[0]
                new_item["frequence"] = index[item]
                if item in inverse_index:
                    inverse_index[item].append(new_item)
                else:
                    inverse_index[item] = [new_item]
    return inverse_index

if __name__ == "__main__":
    inverse_index = build(r"../data/")
    cPickle.dump(inverse_index, gzip.open("inverse_index.p", "wb"))
