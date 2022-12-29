def kelvintofahrenheit(Temperature):
    assert (Temperature >= 0),"colder than absolute zero at MTICA!"
    res=((Temperature-273)*1.8)+32
    return res
try:
    print (kelvintofahrenheit(-50))
except Exception as ob:
    print(ob)
try:
    print (kelvintofahrenheit(273))
except Exception as ob:
    print(ob)
try:
    print (kelvintofahrenheit(505.78))
except Exception as ob:
    print(ob)
try:
    print (kelvintofahrenheit(-5))
except Exception as ob:
    print(ob)    

print("Thank you")
