#global
def f():
    x=10
    def g():
        global x
        x=1

    g()
    print(x)
f()
'''
output:
======
10
'''
