##def printDeatail(name, marks=54,age=20):
##    print("name:",name)
##    print("marks:",marks)
##    print("age:",20)
##    return None
####printDeatail()
##printDeatail('sasi')
##printDeatail('sasikala',89)
##printDeatail(name='sasi',marks=98,age=20)
##

def add(*n):
    temp=0
    for i in n:
        temp+=i
    return  temp

print("add():",add())
print("add(5):",add(5))
print("add(5,7):",add(5,7))
print("add(5,7,2):",add(5,7,2))
print("add(5,7,2,45,67,85,22):",add(5,7,2,45,67,85,22))
