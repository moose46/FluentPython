__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter3-5.py was created on April 22 2022 @ 8:12 AM
# Project: FluentPython
# uses set dict.setdefault to fetch and update a list of word
# occurrences from the index in a single line

import re
import sys

WORD_RE = re.compile("\w+")

if __name__ == '__main__':
    index = {}
    with open('zen_of_python.txt') as fp:
        for line_no,line in enumerate(fp,1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                index.setdefault(word,[]).append(location)

    for word in sorted(index,key=str.upper):
        print(word, index[word])
