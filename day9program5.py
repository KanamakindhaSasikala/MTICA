def printMonthName(dn):
    if(dn==1):
        return "january"
    elif(dn==12):
         return "december"
    elif(dn==10):
         return "october"
    elif(dn==8):
         return "August"
    elif(dn==11):
         return "november"
    elif(dn==6):
         return "june"
    elif(dn==2):
         return "february"
    elif(dn==3):
         return "march"
    elif(dn==5):
         return "may"
    else:
         return "Invalid"
        

for i in range(4):
    inpN=int(input())
    print(printMonthName(inpN))

    
