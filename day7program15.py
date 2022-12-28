#create a list from the elements of a range from 1200-2000with 130 
##ans=[]
##for i in range(1200,2001,130):
##    ans.append(i)
##print(ans)

##ans= [i for i in range(1200,2001,130)]
##print(ans)
##lst=[10,15,20,25,30,35,40,45]
##ans=[]
##for i in lst:
##     ans.append(i*6)
##print(ans)
##ans=[i*6 for i in lst]
##print(ans)

dict1={"sedan": 1500, "suv":2000, "pickup": 2500, "minivan": 1600, "van": 2400,
          "semi": 13600, "bicycle": 3456, "motorcycle": 110}
ans=[]
for i in dict1:
    if dict1[i]<5000:
       ans.append(i.upper())
print(ans)

ans=[i.upper() for i in dict1 if dict1[i]<5000]
print(ans)
