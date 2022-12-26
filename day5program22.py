def remove_vowel(s):
    t_vowel=''
    for i in s:
        if i not in 'AEIOUaeiou':
            t_vowel+=i
    return t_vowel
s1=input()
a=remove_vowel(s1)
print('string',s1,"without vowel",a)

s=input()
vowel=''
for i in s:
    if i in 'AEIOUaeiou':
        vowel+=i
