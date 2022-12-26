def count_vowel(s):
    t_vowel=0
    for i in s:
        if i in 'AEIOUaeiou':
            t_vowel+=1
    return t_vowel
inp=input()
a=count_vowel(inp)
print("vowels=",a)

s=input()
vowel=''
for i in s:
    if i in 'AEIOUaeiou':
        vowel+=i
