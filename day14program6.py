##Overriding:
class Wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Grr....")
class Dog(Wolf):
    def bark(self):
        print("Woof")
pet1=Dog("tomy","brown")

pet1.bark()
pet2=Wolf("jimmy","grey")
pet2.bark()
Dog("abc","xyz").bark()


'''    
output:
===========
Woof
Grr....
Woof

'''
