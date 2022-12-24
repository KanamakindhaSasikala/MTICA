Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lst1=[20,34,'python',34, 'sasi']
lst1.append(20)
lst1
[20, 34, 'python', 34, 'sasi', 20]
lst1
[20, 34, 'python', 34, 'sasi', 20]
lst.append()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    lst.append()
NameError: name 'lst' is not defined. Did you mean: 'lst1'?
lst.append(34)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    lst.append(34)
NameError: name 'lst' is not defined. Did you mean: 'lst1'?
l1=[10,15,20,10,'mca']
l1.append(10)
l1
[10, 15, 20, 10, 'mca', 10]
l1.append('python')
l1
[10, 15, 20, 10, 'mca', 10, 'python']

help(list)

type(4)
<class 'int'>
l1.clear()
l1
[]
l1.count[10]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l1.count[10]
TypeError: 'builtin_function_or_method' object is not subscriptable
l1=[10,20,15,'mca','python']
l1.count(10)
1
l1
[10, 20, 15, 'mca', 'python']
l1.count(20)
1
l1.count(l1)
0
l1.count('python')
1
len(l1)
5
l1.count('mca')
1
del l2[-1]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    del l2[-1]
NameError: name 'l2' is not defined. Did you mean: 'l1'?
l2=[10,15,20,2]
l2
[10, 15, 20, 2]
l1
[10, 20, 15, 'mca', 'python']
l3=l1.copy()
print(id(l1),id(l3))
2366894390912 2366892644800
l1
[10, 20, 15, 'mca', 'python']
l3
[10, 20, 15, 'mca', 'python']
l2
[10, 15, 20, 2]
l3.append(10)
l3
[10, 20, 15, 'mca', 'python', 10]
l3=l1

l3=l1[:]
l3
[10, 20, 15, 'mca', 'python']
