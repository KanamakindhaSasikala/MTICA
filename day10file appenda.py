##n=open (r"D:\pythonpractice_53\day10\file123.txt","a+",)
##for i in range(5):
##    inpstr=input("enter name:")
##    n.write(inpstr+'\n')
##n.close()
##print("written to file")
##        
      
f1=open(r"D:\pythonpractice_53\day10\file123.txt","r",)
f2=open (r"D:\pythonpractice_53\day10\day10file1.txt","w+",)

temp=f1.read()
f2.write(temp)

f1.close()
f2.close()
print("file copied")
