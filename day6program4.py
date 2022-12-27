Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: D:/pythonpractice_53/day6/day6program1.py
enter a value(0 to end):5
enter a value(0 to end):12
enter a value(0 to end):4
enter a value(0 to end):0
[4, 5, 12]
min: 4
max: 12
avg: 7.0

= RESTART: D:/pythonpractice_53/day6/day6program1.py
enter a value(0 to end):67
enter a value(0 to end):87
enter a value(0 to end):87
enter a value(0 to end):98
enter a value(0 to end):0
[67, 87, 87, 98]
min: 67
max: 98
avg: 84.75

= RESTART: D:/pythonpractice_53/day6/day6program1.py
enter a value(0 to end):
    = RESTART: D:/pythonpractice_53/day6/day6program1.py
Traceback (most recent call last):
  File "D:/pythonpractice_53/day6/day6program1.py", line 3, in <module>
    n=int(input("enter a value(0 to end):"))
ValueError: invalid literal for int() with base 10: ''

==================== RESTART: D:/pythonpractice_53/day6/day6program1.py ===================
enter a value(0 to end):4
enter a value(0 to end):6
enter a value(0 to end):7
enter a value(0 to end):8
enter a value(0 to end):0
min: 4
max: 8
avg: 6.25

==================== RESTART: D:/pythonpractice_53/day6/day6program2.py ===================
enter a value(-1 to end):9
enter a value(-1 to end):3
enter a value(-1 to end):6
enter a value(-1 to end):8
enter a value(-1 to end):60
enter a value(-1 to end):5
enter a value(-1 to end):4
enter a value(-1 to end):6
enter a value(-1 to end):3
enter a value(-1 to end):2
enter a value(-1 to end):1
enter a value(-1 to end):0
enter a value(-1 to end):-1
Traceback (most recent call last):
  File "D:/pythonpractice_53/day6/day6program2.py", line 12, in <module>
    lst.sort()
NameError: name 'lst' is not defined. Did you mean: 'list'?

==================== RESTART: D:/pythonpractice_53/day6/day6program2.py ===================
enter a value(-1 to end):3
enter a value(-1 to end):8
enter a value(-1 to end):9
enter a value(-1 to end):7
enter a value(-1 to end):6
enter a value(-1 to end):2
enter a value(-1 to end):0
enter a value(-1 to end):-1
Even: 8 6 2 0
min: 0
max: 8
Traceback (most recent call last):
  File "D:/pythonpractice_53/day6/day6program2.py", line 18, in <module>
    print("avg:",round(sum(lstEven)/len(lstOdd),1))
ZeroDivisionError: division by zero

==================== RESTART: D:/pythonpractice_53/day6/day6program2.py ===================
enter a value(-1 to end):5
enter a value(-1 to end):4
enter a value(-1 to end):6
enter a value(-1 to end):7
enter a value(-1 to end):3
enter a value(-1 to end):2
enter a value(-1 to end):1
enter a value(-1 to end):60
enter a value(-1 to end):-1
Even: 4 6 2 60
min: 2
max: 60
Traceback (most recent call last):
  File "D:/pythonpractice_53/day6/day6program2.py", line 18, in <module>
    print("avg:",round(sum(lstEven)/len(lstOdd),1))
ZeroDivisionError: division by zero

==================== RESTART: D:/pythonpractice_53/day6/day6program2.py ===================
enter a value(-1 to end):1
enter a value(-1 to end):4
enter a value(-1 to end):6
enter a value(-1 to end):7
enter a value(-1 to end):9
enter a value(-1 to end):4
enter a value(-1 to end):6
enter a value(-1 to end):3
enter a value(-1 to end):-1
Even: 4 6 4 6
min: 4
max: 6
avg: 5.0
Odd: 1 7 9 3
min: 1
max: 9
avg: 5.0

==================== RESTART: D:/pythonpractice_53/day6/day6program3.py ===================
one: 5
two: -18
3+4
7
print(3+4)
7
x=3+4
print(x)
7
print(x=3+4)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(x=3+4)
TypeError: 'x' is an invalid keyword argument for print()
print(x==3+4)
True
