__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter3-6.py was created on April 22 2022 @ 8:42 AM
# Project: FluentPython
#
import collections
import re
import sys
from pathlib import Path

PATH = Path.cwd()
WORD_RE = re.compile("\w+")

if __name__ == '__main__':
    index = collections.defaultdict(list)
    with open('zen_of_python.txt') as fp:
        for line_no,line in enumerate(fp,1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                index[word].append(location)

    for word in sorted(index,key=str.upper):
        print(word, index[word])
