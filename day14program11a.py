class Complex:
    def __init__(self,real,image):
        self.real=real
        self.image=image
    def __add__(self,ob):
        temp=self.real+ob.real,self.image+ob.image
        return  temp
    def __str__(self):
        return(self.real,self.image)
ob1=Complex(3,5)
ob2=Complex(2,6)
ob3=ob1+ob2

print(ob3)

'''
output:
==============
(5, 11)
'''
