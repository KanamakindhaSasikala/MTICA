#finding extract special characters
def extract_consonant(s):
    t_consonant=0
    for i in s:
        if i in 'bcdfghjklmnopqrstvwxyz':
            t_consonant+=1
    return t_consonant
inp=input()
a=extract_consonant(inp)
print("consonant=",a)

s=input()
consonant=''
for i in s:
    if i in 'bcdfghjklmnopqrstvwxyz':
        consonant+=i
