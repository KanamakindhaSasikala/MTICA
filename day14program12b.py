class Employee:
    empCount=0
    def __init__(self,name,salary):
       self.name=name
       self.salary=salary
       Employee.empCount+=1
    def displayCount(self):
        print("Total Employee %d "% Employee.empCount)
    def displayEmployee(self):
        print("Name :", self.name, ", Salary: ", self.salary)
emp1=Employee("Akil",9996)
emp1.displayEmployee()
print ("is salary an attribute:",hasattr(emp1, 'salary'))
print(getattr(emp1, 'salary'))   #returns  value of salary attribute
setattr(emp1,'salary',84000)    #set attribute salary
print("Modified salary",getattr(emp1, 'salary'))
print(hasattr(emp1,'desg'))
setattr(emp1, 'desg','manager')
print(hasattr(emp1,'desg'))
print("Added Attribute", getattr(emp1, 'desg'))
delattr(emp1, 'salary')                                  #delete salary atribute
print("is salary an attribute:",hasattr(emp1,'salary'))

'''
output:
==============
Name : Akil , Salary:  9996
is salary an attribute: True
9996
Modified salary 84000
False
True
Added Attribute manager
is salary an attribute: True
==============
#delattr(emp1, 'salary'):
Name : Akil , Salary:  9996
is salary an attribute: True
9996
Modified salary 84000
False
True
Added Attribute manager
is salary an attribute: False
'''
