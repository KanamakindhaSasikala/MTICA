lst=[]
while(True):
   n=int(input("enter a value(0 to end):"))
   if n==0:
        break  
   else:
       lst.append(n)    
lst.sort()
##print(lst)

print("min:",lst[0])
print("max:",lst[-1])
print("avg:",round(sum(lst)/len(lst),3))
