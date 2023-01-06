#nonlocal

def f():
    x=10
    def g():
        nonlocal x
        x=1

    g()
    print(x)
f()
'''
output:
=====
1
'''
