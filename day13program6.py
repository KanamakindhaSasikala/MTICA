def sum_num(x):
     res=0
     for i in range(x+1):
         res=res+i
         yield ("i=",i,"res=",res)
     return res


obj=sum_num(11)
for i in range(11):
     print(next(obj))
         
     
