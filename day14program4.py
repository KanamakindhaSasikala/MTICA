class Wolf:
    price=500
    def __init__(self,name,color):
      self.name=name
      self.color=color
    def bark(self):
        print("Grr...")
class Dog(Wolf):
    def bark1(self):
        print("Woof")
if __name__=="__main__":
   pet1=Dog("tomy","brown")
   pet1.bark()
   pet1.bark1()
   print(pet1.name,"is of color",pet1.color)

output:
=====================
'''
Grr...
Woof
tomy is of color brown
'''
