# !/usr/bin/env python
# coding=utf8
# Author: quheng
import os
import cPickle
import re
import gzip
import nltk
from nltk.tokenize import wordpunct_tokenize 


def build(path):
    stemmer = nltk.PorterStemmer()
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
            words = wordpunct_tokenize(f.read())
            index = {}
            for word in words:
                word = word.strip(' ,\n')
                try:
                    word = stemmer.stem(word)
                    if not word:
                        continue
                    if word in index:
                        index[word] += 1
                    else:
                        index[word] = 1
                except Exception, e:
                    continue
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
    # cPickle.dump(inverse_index, gzip.open("inverse_index.p", "wb"))
    cPickle.dump(inverse_index, open("inverse_index.p", "wb"))

