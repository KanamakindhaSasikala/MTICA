def  reverseString(s):
     a=[i[::-1]for i in s]
     return a
     

n=input().split()
print(n)
print(*reverseString(n))
