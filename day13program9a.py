##def squares(x=0):
##    while x<10 :
##        x=x+1
##        yield x*x
##yieldedList=[i for i in squares()]
##print(yieldedList)
##
####MaterialiseList from generator using list()
##yieldList=list(squares())
##print(yieldedList)


def  cal_Cubic():
     i=1;
     while True:
         yield i*i*i
         i +=1

for i in cal_Cubic():
    if i>1000:
        break
    print(i)
