def outer():
    message='outer function'
    print(message)
    def inner():
        print(message)
    inner()
outer()
'''
output:
=========
outer function
outer function
'''
