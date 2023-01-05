class Dog:
  price=400
  def __init__(self,name,color):
     self.color=color
     self.name=name
  def bark(self):
     print("woof")
     print(self.name,"has",self.price,"price and its color is",self.color)             
if __name__=='__main__':
    pet1=Dog("Tommy","brown")
    pet2=Dog("Sheru","white")
    pet1.bark()
    pet2.bark()
    print(pet1.price)
    print(pet1.price)
    print(Dog.price)
    Dog('abc','blue').bark()

output:
====================
'''
woof
Tommy has 400 price and its color is brown
woof
Sheru has 400 price and its color is white
400
400
400
woof
abc has 400 price and its color is blue
'''

