def printDay(dn):
    if(dn==1):
        return "monday"
    elif(dn==2):
         return "tuesday"
    elif(dn==3):
         return "wednesday"
    elif(dn==4):
         return "thursday"
    elif(dn==5):
         return "friday"
    elif(dn==6):
         return "saturday"

    else:
         return "0 or-ve Invalid"
        
import time
for i in range(4):
    inpN=int(input())
    start=time.time()
    print(printDay(inpN))
    print(time.time()-start)
##    start=time.time() 
##    print(printdayName(inpN))
##    print=(time.time()-start)
##
