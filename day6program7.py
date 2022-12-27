##m.floor(9.7)
##9
##m.ceil(9.1)
##10
##m.log(1024,2)
##10.0
##m.log(16,2)
##4.0
##m.log(25,5)
##2.0
===============================================
import math
math.pi
3.141592653589793
import math
math.pi=43
math.pi
43
==================================================

===============================
import math
math.sqrt(2)
1.4142135623730951
math.gcd(24,40)
8
============================
from math import *
sqrt(2)
1.4142135623730951
gcd(6)
6
============================
from math import sqrt,gcd
sqrt(9)
3.0
gcd(65,87)
1
==============================
import math as m
m.sqrt(6)
2.449489742783178
m.gcd(35,76)
1
m.gcd(24,40)
8
##==============
print('{0},{1},{2}'.format('apple','banana','carrot','pen'))
##apple,banana,carrot
print('{0},{1}{0}{0}{3},{2}'.formate('apple','banana','carrot','pen'))
print('{0},{1}{0}{0}{3},{2}'.format('apple','banana','carrot','pen'))
##apple,bananaappleapplepen,carrot
print('{0},{1},{0},{0},{3}{2}'.format('apple','banana','carrot','pen'))
##apple,banana,apple,apple,pencarrot
print('{0},{1},{0},{3}, {2}, {2}'.format('apple','banana','carrot','pen'))
##apple,banana,apple,pen, carrot, carrot
print('{}, {}, {}'.format('apple', 'banana',  'carrot'))
##apple, banana, carrot
print('gangully purchased a kg of{},a dozen of {}and half kg of{}'.format('apple',  'banana',  'carrot'))
##gangully purchased a kg ofapple,a dozen of bananaand half kg ofcarrot
##=======================================================
x,*y,z='computer'
x
'c'
y
['o', 'm', 'p', 'u', 't', 'e']
z
'r'
*x,y='abcd'
x
['a', 'b', 'c']
y
'd'
print('{2}, {1}, {0}'.format(*'abcd'))
c, b, a
##======================================================================
print('coordinates:{latitude},{longitude}'.format(latitude='37.24n',longitude='-115.81w'))
      
coordinates:37.24n,-115.81w

student={48:'Teja',43:'sufiya'}
      
type(student)
      
<class 'dict'>
student
      
{48: 'Teja', 43: 'sufiya'}
student.keys
      
<built-in method keys of dict object at 0x0000027C3DCAF7C0>
student.kets()
      
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    student.kets()
AttributeError: 'dict' object has no attribute 'kets'. Did you mean: 'keys'?
student.keys()
      
dict_keys([48, 43])
student.values()
      
dict_values(['Teja', 'sufiya'])
