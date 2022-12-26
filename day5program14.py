##def checkanagram(s1,s2):
##    if sorted(s1)==sorted(s2):
##        return 'yes'
##    else:
##        return 'no'
##inp=input().split()
##print(checkanagram(inp[0],inp[1]))

def extract_vowel(s):
     temp_vowel=''
     for i in s:
         if i in 'AEIOUaeiou':
             temp_vowel+=i
     return temp_vowel
inp=input()
a=extract_vowel(inp)
print("vowel is=",a)
print(len(a))
'''
s=input()
temp_vowel="
for i in s:
     for i in'AEIOUaeiou':
         temp_vowel+=i
print("vowels",temp_vowel)'''
a=extract_vowel(s)
print("vowels:",a)
      
