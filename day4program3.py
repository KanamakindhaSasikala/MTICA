
##import  math
##def checkprimenumber(num):
##     if num<1:
##           return 0
##     if num==1 or num==2 or num==3:
##         return num
##     count=num//2 +1         
##     for i in range(2,count):
##          if num%i==0:
##                return 0
##     return num
##f=int(input())
##l=int(input())
##lst=[]
##for j in range(f,l+1):
##    if checkprimenumber(j):
##       lst.append(j)                      
##print(*lst)
##print(len(lst))

import math
n=imput()
total=0
for i in n:
      total=pow(int(i),length(n))
if n==total:
    print(n,"is armstrong number")
else:
    print(n,"is not a armstrong number")
    
