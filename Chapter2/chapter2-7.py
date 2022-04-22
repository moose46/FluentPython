__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'


#
# Author: Robert W. Curtiss
# chapter2-7.py was created on April 19 2022 @ 10:46 AM
# Project: FluentPython
# Tuples used as records

def main():
    print(f'{"":15} | {"Latitude":>9} | {"Longitude":>9}')
    for name,_,_,(lat,lon) in metro_areas:
        if lon <=0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

if __name__ == '__main__':
    lax_corrdinates = (33.9425, -118.408056)
    city, year, pop, chg, area = ('Toyko', 2003, 32_450, 0.66, 8014)
    traveler_ids = [('USA', '31185855', 'C'), ('BRA', 'CE342567', 'D'), ('ESP', 'XDA2055856', 'F')]

    for passport in sorted(traveler_ids):
        print(passport)
        print("%s/%s %s" % passport)
    for country, _, _ in traveler_ids:
        print(country)

    lat, long = lax_corrdinates  # upacking
    print(lat, long)

    print(divmod(20, 8))
    quotient, remainder = divmod(20, 8)
    print(quotient, remainder)

    import os

    _, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')
    print(os.path.split('/home/luciano/.ssh/id_rsa.pub'))
    print(filename)

    # Nested un packing
    metro_areas = [
        ('Toyko', 'JP', 36.933,(35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889 , 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 28.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),

    ]
    main()
