def div(a,b):
    assert( isinstance(a,int) or isinstance(a,float)),\
             'First Argument should be either integer or float'
    assert( isinstance(b,int) or isinstance(b,float)),\
             'second Argument should be either integer or float'        
    assert (b!=0),"Division by zero is not defined"
    return a/b

try:
    print (div(55,0))
except AssertionError as obj:
    print(obj)
try:
    print (div(23,4))
except AssertionError as obj:
    print(obj)
try:
    print (div(20,'world'))
except AssertionError as obj:
    print(obj)
try:
    print (div('hello',9))
except AssertionError as obj:
    print(obj)
try:
    print (div(20,8))
except AssertionError as obj:
    print(obj)
try:
    print (div(63,4))
except AssertionError as obj:
    print(obj)
print("Thank you")    
