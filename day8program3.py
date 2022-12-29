def Factorial(num):
    assert (isinstance(num,int)),"Factorial  is not defined for non integer"
    assert (num>=0),"Factorial of negative number is not defined!"
    if num==0:
        return  1
    else:
        return num*Factorial(num-1)
try:
    print (Factorial(-45))
except Exception as ob:
    print(ob)    
try:
    print (Factorial(-4.9))
except Exception as ob:
    print(ob)
try:
    print (Factorial(43))
except Exception as ob:
    print(ob)
try:
    print (Factorial(57))
except Exception as ob:
    print(ob)
try:
    print (Factorial(4.2))
except Exception as ob:
    print(ob)

print("Thank you")
