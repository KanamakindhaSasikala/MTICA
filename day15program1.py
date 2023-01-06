n1=input().split()
n2=input().split()
a=[]
for i,j in zip(n1,n2):
    a.append(int(i)+int(j))
print(*a)

 '''
output:
===========
11 22 33
1 2 3
12 24 36
'''
