import functools as ft
def sum(*args):
    print(ft.reduce(lambda x,y:x+y, args ))

sum(1,2,3,4,5)