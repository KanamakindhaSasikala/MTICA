#finding extract special characters
def extract_special(s):

    t_special=0
    for i in s:
        if i in '@,#,<<,>,$,&,^,%,*,!,<=':
            t_special+=1
    return t_special
inp=input()
a=extract_special(inp)
print("special=",a)

s=input()
special=''
for i in s:
    if i in '@,#,<<,>,$,&,^,%,*,!,<=':
        special+=i
