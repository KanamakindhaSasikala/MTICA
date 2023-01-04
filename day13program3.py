def printSunday():
    print("Sunday")
def printMonday():
    print("Monday")
def printTuesday():
    print("Tuesday")
def printWednesday():
    print("Wednesday")
def printThursday():
    print("Thursday")
def printFriday():
    print("Friday")
def printSaturday():
    print("Saturday")
def choice():
    print("Enter day number between 1-7")
dayDict={1:printSunday, 2:printMonday,3:printTuesday,4:printWednesday,
        5:printThursday,6:printFriday,7:printSaturday}
choice()
dayNo=int(input())
if dayNo>=1 and dayNo<=7:
    dayDict[dayNo]()
else:
    print("INVALID")
   
