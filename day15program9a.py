def f():
    x=10
    print('id(x) in f outer:',id(x))
    def g():
        nonlocal x
        x=15
        print('id(x) in f inner:',id(x))
    g()
    print(x)
f()

'''
output:
===============
id(x) in f outer: 140720572646472
id(x) in f inner: 140720572646632
15
'''
