#finding extract special characters
def count_special(s):

    t_special=0
    for i in s:
        if i in '@,#,<<,>,$,&,^,%,*,!,<=':
            t_special+=1
    return t_special
inp=input()
a=count_special(inp)
print("special=",a)

s=input()
special=''
for i in s:
    if i in '@,#,<<,>,$,&,^,%,*,!,<=':
        special+=i
