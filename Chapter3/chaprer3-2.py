__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chaprer3-2.py was created on April 21 2022 @ 9:04 AM
# Project: FluentPython
# Pattern Matching with mappings



def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f'Invalid book record: {record!r}')
        case _:
            raise ValueError(f"Invalid record: {record!r}")



if __name__ == '__main__':
    book1 = dict(api=1,author='Douglas Hofstader', type='book',title='Godel, Escher, Bach')
    r1 = get_creators(book1)
    from collections import OrderedDict
    book2 = OrderedDict(api=2,type='book',
                        title='Python in a Nutshell',authors='Martelli Ravencroft Holden'.split(), )
    r2 = get_creators(book2)

    food = dict(category='ice cream', flavor='vanilla', cost=199)
    match food:
        case {'category': 'ice cream', **details}:
            print(f'Ice Cream details: {details}')
    tt = (1,2,(30,40))
    h = hash(tt)
    tt = (1,2,[30,40])
    # h1 = hash(tt)
    import this

