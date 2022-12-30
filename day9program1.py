##def printSeriesIncreasing(ch,n):
##    for i in range(1,n+1,1):
##         print(ch*i)
##    return None
##def printSeriesDecreasing(ch,n):
##    for i in range(n,0,-1):
##        print(ch*i)
##    return None
##nch=input("enter a character:")
##

def printSeriesDecreasing(ch,n):
    assert isinstance(ch,str),'first argument shoud be string'
    assert isinstance(n,int),'second argument shoud be int'
    for i in range(n,0,-1):
        print(ch*i)
    return None
inpch=input("enter a character:")
inpNum=int(input("enter a number:"))

print('-',20)
try:
    printSeriesDecreasing(inpch,inpNum)
except AssertionError as ob:
     print(ob)
     
##printSeriesDecreasing(inpch,inpNum)
