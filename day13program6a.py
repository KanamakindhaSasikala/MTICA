def demo_yield(x):
     res=0
     for i in range(x+1):
         res=res+i
         yield ("i=",i,"res=",res)
     return res
n=int(input())
g_obj=demo_yield(n)
for i in range(n+1):
    print(next(g_obj))
##obj=sum_num(11)
##for i in range(11):
##     print(next(obj))
##         
     
