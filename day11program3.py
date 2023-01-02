def findFrequency(s):
    frequencyDict=dict()             #empty dictionary
    for i in s:
           if i in frequencyDict:
               frequencyDict[i] +=1
           else:
               frequencyDict[i]=1      #get dictionary element
    return frequencyDict       
def formatOutput(d):
    for i in sorted(d):          #key and value sorted
        print(i,d[i])
n=int(input())
for i in range(n):
     inpstr=input()
     formatOutput(findFrequency(inpstr))
