#non negative integers(factors):
def  findfactor(n):
     temp=list()
     for i in range(1,n+1):
         if n%i==0:
             temp.append(i)
     return  temp
        
a=int(input())
print(*findfactor(a))

'''
output:
==========
30
1 2 3 5 6 10 15 30
'''
