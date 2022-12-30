def printSeries(ch,n):
    sp='.'
    for i in range(1,n):
        print(sp*(n-i-1) +ch*(2*i-1)+sp*(n-i-1))
    return None

inpch=input()
inpNum=int(input())
printSeries(inpch,inpNum)

##*
##5
##....*....
##...***...
##..*****..
##.*******.
##*********
*
5
...*...
..***..
.*****.
*******
