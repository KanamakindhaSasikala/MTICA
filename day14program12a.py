class Employee:
    empCount=0
    def __init__(self,name,salary):
       self.name=name
       self.salary=salary
       Employee.empCount+=1
    def displayCount(self):
        print("Total Employee :",Employee.empCount)
    def displayEmployee(self):
        print("Name :", self.name, ", Salary: ", self.salary)
emp1=Employee("Akil",9996)
emp1.displayEmployee() #modify salary
emp1.salary=56000
emp1.experience=5          #add an exp attribute
emp1.displayEmployee()
emp1.name='Arjun'            #modify 'name' attribute
emp1.displayEmployee()
print(emp1.experience)
#del emp1.salary             #delete employee salary
emp1.displayEmployee()


'''
output:
===========
Name : Akil , Salary:  9996
Name : Akil , Salary:  56000
Name : Arjun , Salary:  56000
5
Name : Arjun , Salary:  56000


#del emp1.salary:
=============
Name : Akil ,Salary:  9996
Name : Akil ,Salary:  56000
Name : Arjun ,Salary:  56000
3
'''
