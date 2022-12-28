#create a list from the elements of a range from 1200-2000with 130 
##ans=[]
##for i in range(1200,2001,130):
##    ans.append(i)
##print(ans)

##ans= [i for i in range(1200,2001,130)]
##print(ans)


lst=[10,15,20,25,30,35,40,45]
##ans=[]
##for i in lst:
##     ans.append(i+6)
##print(ans)

ans=[i*6 for i in lst]
print(ans)
