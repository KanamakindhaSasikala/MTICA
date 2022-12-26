Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: D:/pythonpractice_53/day5/day5program4.py
s0: *	*
**	**
***	***

s1: I said,"This is a valid string."
s1='"Hi mom",I said. "How are you?"'
s1
'"Hi mom",I said. "How are you?"'
print(s1)
"Hi mom",I said. "How are you?"
s2='"Hi mom",I said. '"How are you?"
s2
'"Hi mom",I said. How are you?'
print(s2)
"Hi mom",I said. How are you?
s3='"Hi mom",I said. '"How are you?"'
SyntaxError: unterminated string literal (detected at line 1)
s3='"Hi mom",I said. '"How are you?"'
SyntaxError: unterminated string literal (detected at line 1)
SyntaxError: unterminated string literal (detected at line 1)
SyntaxError: invalid syntax. Perhaps you forgot a comma?


s3='"Hi mom",I said. '"How are you?"'
SyntaxError: unterminated string literal (detected at line 1)
s3='"Hi mom",I said. ''"How are you?"'
s3
'"Hi mom",I said. "How are you?"'
print(s3)
"Hi mom",I said. "How are you?"
s4="""'Hi mom",I said. '"How are you?"'"""
s4
'\'Hi mom",I said. \'"How are you?"\''
print(s4)
'Hi mom",I said. '"How are you?"'
s5=""I want to be alion tamer!""
SyntaxError: invalid syntax
KeyboardInterrupt
s5=""i want to be alion tamer!""
SyntaxError: invalid syntax
KeyboardInterrupt
KeyboardInterrupt
s5="I want to be alion tamer!"
s5
'I want to be alion tamer!'
print(s5)
I want to be alion tamer!
s6="\"Is this a cheese shop?\"\n\t'yes'\n\t"we have all kinds\""
SyntaxError: invalid syntax
s6="\"Is this a cheese shop?\"\n\t'yes'\n\t'we have all kinds\'"
s6
'"Is this a cheese shop?"\n\t\'yes\'\n\t\'we have all kinds\''
print(s6)
"Is this a cheese shop?"
	'yes'
	'we have all kinds'
s="Cats\tare\n\tgood\tsources\n\t\tof\tinternet\tmemes"
s
'Cats\tare\n\tgood\tsources\n\t\tof\tinternet\tmemes'
print(s)
Cats	are
	good	sources
		of	internet	memes

= RESTART: D:/pythonpractice_53/day5/day5program5.py
\\\\
\
\
\

Good-bye
'abc' 'def'
'abcdef'
'abc'+'def'
'abcdef'
'abc '+'def'
'abc def'
x='abc'
y='def'
x
'abc'
+
x+y
'abcdef'
x y
SyntaxError: invalid syntax
s1='abc'*4
s1
'abcabcabcabc'
s2='abc '*4
s2
'abc abc abc abc '

= RESTART: D:/pythonpractice_53/day5/day5program6.py
6
6
8

= RESTART: D:/pythonpractice_53/day5/day5program6.py
6
6
17

= RESTART: D:/pythonpractice_53/day5/day5program6.py
6
6
10

= RESTART: D:/pythonpractice_53/day5/day5program6.py
6
6
10

= RESTART: D:/pythonpractice_53/day5/day5program6.py
6
6
8
'abc'+str(5)
'abc5'
'abc'*str(5)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    'abc'*str(5)
TypeError: can't multiply sequence by non-int of type 'str'
'abc'+5
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    'abc'+5
TypeError: can only concatenate str (not "int") to str
'abc'*5
'abcabcabcabcabc'

'abc'+5.0
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    'abc'+5.0
TypeError: can only concatenate str (not "float") to str
'abc+float(5.0)
SyntaxError: unterminated string literal (detected at line 1)
'abc'+float(5.0)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    'abc'+float(5.0)
TypeError: can only concatenate str (not "float") to str
str(3.0)*3
'3.03.03.0'

= RESTART: D:/pythonpractice_53/day5/day5program11.py
enter an integer==>4
x is: 88

= RESTART: D:/pythonpractice_53/day5/day5program12.py
enter an integer==>64
64 , 6 6

= RESTART: D:/pythonpractice_53/day5/day5program13.py
mca
Traceback (most recent call last):
  File "D:/pythonpractice_53/day5/day5program13.py", line 7, in <module>
    print(checkanagram(inp[0],inp[1]))
IndexError: list index out of range
