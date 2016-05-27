# !/usr/bin/env python
# coding=utf8
# Author: quheng
import os

def build(path):
    dic_set = set()
    list_of_files = {}
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            f = open(dirpath + filename, 'r')
            words = f.read().split(' ')
            for word in words:
                dic_set.add(word.strip(' ,\n'))
    return dic_set

if __name__ == "__main__":
    dic_set = build(r"/Users/quheng/Documents/Workspace/python/website/flask/HaSearch/data/")
    f = open('big.txt', 'w')
    for word in dic_set:
        f.write(word + ' ')
