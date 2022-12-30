##pattern program
##def  printSeries(n):
##n=int(input("enter a number of rows:"))
##for i in range(1,n+1):
##         for j in range(1,n+1):
##              print(i,end=' ')
##              
##         print()
def printSeries(n):
    for i in range(1,n+1):
        print()
        for j in range(i):
            print(i,end=' ')
    return None

inpNum=int(input())
printSeries(inpNum)

output:            
5

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
