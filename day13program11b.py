##x=-1
##x=int(input())
##if x<0:
##    raise Exception("Sorry,no numbers below zero")
##

##x="hello"
##if not type(x) is int:
##   raise TypeError("Only integers are allowed")
##


a=0
b=9
try:                            #condition for checking for negative  values          
    if a<0 or b<0:
        # raising exception using raise keyword
         raise ZerodivisionError
     print(a/b)
except ZerodivisionError:
     print("Please enter valid integer value")
     
