class Vehicle():
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vehicle):
    pass
School_bus=Bus("School Volve",180,12)
print("Vehicle Name:",School_bus.name,"Speed:",
       School_bus.max_speed,"Mileage:",School_bus.mileage)


'''
output:
================
Vehicle Name: School Volve Speed: 180 Mileage: 12
'''

