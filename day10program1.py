Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dict1={'name': 'sasikala', 'age': '20', 'course': 'mca',}
print(dict1(name))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(dict1(name))
NameError: name 'name' is not defined
print(dict1['name'])
sasikala
print(dict1['course'])
mca
dict1['age']=22
print(dict1)
{'name': 'sasikala', 'age': 22, 'course': 'mca'}
dict1['college']='students'
print(dict1)
{'name': 'sasikala', 'age': 22, 'course': 'mca', 'college': 'students'}
del dict1['age']
print(dict1)
{'name': 'sasikala', 'course': 'mca', 'college': 'students'}
dict1.clear()
print(dict1)
{}
dict1={'name': 'sasikala', 'age': 22, 'course': 'mca'}
print(dict1)
{'name': 'sasikala', 'age': 22, 'course': 'mca'}
del dict1
print(dict1)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(dict1)
NameError: name 'dict1' is not defined. Did you mean: 'dict'?
dict1.keys()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict1.keys()
NameError: name 'dict1' is not defined. Did you mean: 'dict'?
dict1={'name': 'sasikala', 'age': 22, 'course': 'mca'}
dict1.keys()
dict_keys(['name', 'age', 'course'])
dict1-values()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict1-values()
NameError: name 'values' is not defined
dict1_values()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    dict1_values()
NameError: name 'dict1_values' is not defined
dict.values()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dict.values()
TypeError: unbound method dict.values() needs an argument
dict1.values()
dict_values(['sasikala', 22, 'mca'])
dict1.items()
dict_items([('name', 'sasikala'), ('age', 22), ('course', 'mca')])
for i in dict1:print(i)

name
age
course
for i in dict1.keys():print(i)

name
age
course
for i,j in dict1.items():print(i,j)

name sasikala
age 22
course mca
