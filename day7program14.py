Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============== RESTART: D:/pythonpractice_53/day7/day7program13.py =============
[100, 225, 625, 900, 1600]

============== RESTART: D:/pythonpractice_53/day7/day7program13.py =============
[100, 225, 625, 900, 1600]
dict1={"sedan": 1500, "suv":2000, "pickup": 2500, "minivan": 1600, "van": 2400, "semi": 13600. "bicycle": 3456, "motorcycle": 11120}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
dict1={"sedan": 1500, "suv":2000, "pickup": 2500, "minivan": 1600, "van": 2400, "semi": 13600, "bicycle": 3456, "motorcycle": 11120}
dict1
{'sedan': 1500, 'suv': 2000, 'pickup': 2500, 'minivan': 1600, 'van': 2400, 'semi': 13600, 'bicycle': 3456, 'motorcycle': 11120}
dict1.keys()
dict_keys(['sedan', 'suv', 'pickup', 'minivan', 'van', 'semi', 'bicycle', 'motorcycle'])
dict.values()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dict.values()
TypeError: unbound method dict.values() needs an argument
dict1.values()
dict_values([1500, 2000, 2500, 1600, 2400, 13600, 3456, 11120])
dict1.items()
dict_items([('sedan', 1500), ('suv', 2000), ('pickup', 2500), ('minivan', 1600), ('van', 2400), ('semi', 13600), ('bicycle', 3456), ('motorcycle', 11120)])

for i in dict1:
     print(i)

    
sedan
suv
pickup
minivan
van
semi
bicycle
motorcycle
for i in dict1:
    print(i+1)

    
Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    print(i+1)
TypeError: can only concatenate str (not "int") to str
for i in dict1:
     print([i])

     
['sedan']
['suv']
['pickup']
['minivan']
['van']
['semi']
['bicycle']
['motorcycle']
for i in dict1:
     print([i]+i)

     
Traceback (most recent call last):
  File "<pyshell#17>", line 2, in <module>
    print([i]+i)
TypeError: can only concatenate list (not "str") to list
for i in dict1:
     print(i,dict1[i])

     
sedan 1500
suv 2000
pickup 2500
minivan 1600
van 2400
semi 13600
bicycle 3456
motorcycle 11120
for i in dict1:
      if dict1[i]<5000:print(i)

      
sedan
suv
pickup
minivan
van
bicycle
