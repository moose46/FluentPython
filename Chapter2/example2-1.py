__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter2-1.py was created on April 19 2022 @ 9:19 AM
# Project: FluentPython
#


if __name__ == '__main__':
    # https://unicode-table.com/en/search/?q=8364
    symbols = '$¢£¥€¤'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    print(f'{codes}')

    codes = [ord(symbol) for symbol in symbols]
    print(f'{codes}')
