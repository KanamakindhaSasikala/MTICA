fo=open(r"D:/pythonpractice_53/day9/file123.txt","w+")
inpStr=input('enter text:')
fo.write(inpStr)
inpStr=input('enter text:')
fo.write(inpStr)

fo.close()
print('Text written to File')
