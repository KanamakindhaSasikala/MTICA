months={1:'january',2:'february',3:'march',4:'april',5:'may',6:'june',7:'july',
        8:'august',9:'september',10:'octomber',11:'november',12:'december',}
n=int(input())

mn=int(input())

for i in range(n):
    if mn>=1 and mn<=12:
        print(months[n])
    else:
        print("INVALID")
    
