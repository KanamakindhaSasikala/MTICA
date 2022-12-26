def count_digits(s):
    t_digits=0
    for i in s:
        if i in '012345678':
            t_digits+=1
    return t_digits
inp=input()
a=count_digits(inp)
print("digits=",a)

s=input()
digits=''
for i in s:
    if i in '012345678':
        digits+=i
