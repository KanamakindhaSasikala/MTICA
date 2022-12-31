n=open (r"D:\pythonpractice_53\day10\file123.txt","a+",)
for i in range(5):
    inpstr=input("enter name:")
    n.write(inpstr+'\n')
n.close()
print("written to file")
        
      
