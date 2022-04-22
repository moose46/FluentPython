__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# example2-10.py was created on April 19 2022 @ 4:33 PM
# Project: FluentPython
# Destructuring nested tuples -- requires python >= 3.10
# https://fpy.li/2-10

metro_areas = [
    ('Toyko', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 28.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),

]

if __name__ == '__main__':
    print(f'{"":15} | {"Latitude":>9} | {"Longitude":>9}')
    for record in metro_areas:
        match record:
            case [name,_,_,(lat,lon)] if lon <=0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
