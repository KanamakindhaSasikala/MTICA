#prime factors
from math import sqrt
def checkPrime(n):
     if n==1 or n==2 or n==3:
         return n
     for i in range(2,int(sqrt(n))+1):
         if n%i==0:
             return None
     return n
        
def  findPrimeFactor(n):
     temp=list()
     for i in range(1,n+1):
         if n%i==0:
             if checkPrime(i):
                 temp.append(i)
     return  temp
    
a=int(input())
#b=int(input())
print(*findPrimeFactor(a))

'''
output:
==========
33
1 3 11
==========
90
1 2 3 5
==========
70
1 2 5 7
'''
