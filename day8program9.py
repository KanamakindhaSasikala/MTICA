##num1=int(input("enter a no:")) 
def CheckEvenOdd(num1):
    assert(num1>0),"Negative numbers"
    if num1%2==0:
        return "Even"
    else:
        return "Odd"

for i in range(3):
    num1=int(input("Enter a no:"))
    try:
        print(num1,"is",checkEvenodd(num1))
    except AssertionError as a:
        print(a)
        

            
