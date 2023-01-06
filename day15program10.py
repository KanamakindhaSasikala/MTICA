message='global scope'
def outer():
    def inner():
        print(message)
    inner()
        
    
outer()
'''
output:
=========
global scope
'''
