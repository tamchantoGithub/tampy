import sys

from django.db.models.fields import return_None

print(sys.getrecursionlimit()) ##1000

sys.setrecursionlimit((1010))

def fact(n):
    if n==0:
        return  1
    else:
        return n*fact(n-1)

print(fact(1000))

def foo(n):
    if n==0:
        print('recursion call finished')
        return
    else:
        foo(n-1)

sys.setrecursionlimit(1000000)
foo(100000)