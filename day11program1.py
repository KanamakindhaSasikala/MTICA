def printMonthname(dn):
    if(dn==1):
        return 'january'
    elif(dn==3):
        return 'march'
    elif(dn==2):
        return 'february'
    elif(dn==4):
        return 'april'
    elif(dn==5):
        return 'may'
    elif(dn==6):
        return 'june'
    elif(dn==8):
        return 'august'
    elif(dn==11):
        return 'november'
    elif(dn==12):
        return 'december'
    else:
        return 'INVALID'

import time
for i  in range(5):
    n=int(input())
    print(printMonthname(n))
    
