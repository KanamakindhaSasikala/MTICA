def squares(x=0):
    while x<10 :
        x=x+1
        yield x*x
yieldedList=[i for i in squares()]
print(yieldedList)

##MaterialiseList from generator using list()
yieldList=list(squares())
print(yieldedList)
