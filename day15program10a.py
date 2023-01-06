message='outer scope'
def outer():
    print(message)
    def inner():
         nonlocal message
         message='inner scope'
         print('inner:',message)
    inner()
    print('outer:',message)    
    
outer()
'''
output:
=========
outer scope
inner: inner scope
outer: inner scope
'''
