__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
#
# Author: Robert W. Curtiss
# registration.py was created on May 20 2022 @ 4:17 PM
# Project: FluentPython
#

registry = []


def register(func):
    print(f'running register({func}')
    registry.append(func)
    return func


@register
def f1():
    print('running f1')


@register
def f2():
    print('running f2')


def f3():
    print('running f3')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
