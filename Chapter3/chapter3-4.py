__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter3-4.py was created on April 21 2022 @ 3:44 PM
# Project: FluentPython
#

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
                # this is ugly
                occurrences = index.get(word,[])
                occurrences.append(location)
                index[word] = occurrences

    for word in sorted(index,key=str.upper):
        print(word, index[word])

