def printMonthName(dn):
    mn=''
    if(dn==1):
        mn='january'
    if(dn==12):
        mn='december'
    if(dn==10):
        mn='october'
    if(dn==8):
        mn='August'
    if(dn==11):
        mn='november'
    if(dn==6):
        mn= 'june'
    if(dn==2):
        mn='february'
    if(dn==3):
        mn='march'
    if(dn==5):
        mn='may'
    else:
        mn='Invalid'
    return mn  

for i in range(5):
    inpN=int(input())
    printMonthName(inpN)
