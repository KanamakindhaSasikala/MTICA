import sys
print("Coming through stdout")
save_stdout=sys.stdout
fh=open(r"D:\pythonpractice_53\day17.txt","w")
sys.stdout=fh
print("this line goes to test.txt")
print(input())
sys.stdout=save_stdout
fh.close()

'''
output:
===============
Coming through stdout
'''
