'''nums=[11,22,33,44,55]
import math
print(nums)

result=list(map(math.sqrt,nums))
print(result)
 
result=[math.sqrt(i) for i in nums]


result=[]
for i in nums:
 '''
def add_five(x):
    temp=x+5
    return temp

nums=[11,22,33,44,55]
result=list(map(add_five,nums))
print(nums)
print(result)
print(' _ '*40)

result=[i+5 for i in nums ]
print(result)
