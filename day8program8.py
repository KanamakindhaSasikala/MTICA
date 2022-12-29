##num1=int(input("enter a no:"))
##if num1%2==0:
##    print(num1, 'is even')
##if num1%2==1:
##    print(num1, 'is odd')
##
##print("we learnt if keyword")
##
num1=int(input("enter a no:"))
def checkEven(num1):
    if num1%2==0:
        return "even" 

def checkOdd(num1):
     if num1%2==1:
        return  "Odd"
##print(checkEven(num1))
##print(checkOdd(num1))
x=checkEven(num1)
y=checkOdd(num1)
print("x=",x)
print("y=",y)
print(checkEven(num1))
print(checkOdd(num1))
