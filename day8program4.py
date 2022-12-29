def div(a,b):
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
    print (div(100,20))
except AssertionError as obj:
    print(obj)
try:
    print (div(45,9))
except AssertionError as obj:
    print(obj)
try:
    print (div(4,8))
except AssertionError as obj:
    print(obj)
try:
    print (div(63,4))
except AssertionError as obj:
    print(obj)
print("Thank you")    
