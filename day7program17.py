##for i in range(5):
##    inp=input()
##    if inp:
##        print("hello  "+inp)
##    else:
##        print("bye  "+inp)
##        

lst=["sedan","suv", "","",'',' ']
ans=[]
for i in lst:
    if i:
        ans.append(i)
print(ans)

ans=[i for i in lst if i]
print(ans)
