Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> def thing():
	print("Hello")
	print("Fun")

	
>>> thing()
Hello
Fun
>>> print("Zip")
Zip
>>> big = max("Hello world")
>>> print(big)
w
>>> tiny = min("Hello world")
>>> print(tiny)
 
>>> print(float(99) / 100)
0.99
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(1 + 2 * float(3) / 4 - 5)
-2.5
>>> sval = "123"
>>> type(sval)
<type 'str'>
>>> print(sval + 1)

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(sval + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> print(ival + 1)
124
>>> def print_lyrics():
	print("I`m a lumberjack")
	print("I sleep all night")

	
>>> x = 5
>>> print("Hello")
Hello
>>> print("Yo")
Yo
>>> x = x + 2
>>> print(x)
7
>>> print_lyrics():
	
SyntaxError: invalid syntax
>>> print_lyrics()
I`m a lumberjack
I sleep all night
>>> 
================== RESTART: /home/user/RTR105/skripts_11.py ==================
>>> greet("en")
Hello
>>> greet("es")
Hola
>>> greet("fr")
Bonjour
>>> def greet():
	return "Hello"

>>> print(greet(), "Don")
('Hello', 'Don')
>>> def addtwo(a, b):
	added = a + b
	return added

>>> x = addtwo(3, 5)
>>> print(x)
8
>>> 
================== RESTART: /home/user/RTR105/skripts_12.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/skripts_12.py", line 7, in <module>
    input(hrs)
NameError: name 'hrs' is not defined
>>> 
================== RESTART: /home/user/RTR105/skripts_12.py ==================
Enter hours:45
Enter rate:10

Traceback (most recent call last):
  File "/home/user/RTR105/skripts_12.py", line 9, in <module>
    computepay()
TypeError: computepay() takes exactly 2 arguments (0 given)
>>> 
================== RESTART: /home/user/RTR105/skripts_12.py ==================
Enter hours:45
Enter rate:10
>>> 
================== RESTART: /home/user/RTR105/skripts_12.py ==================
Enter hours:45
Enter rate:10
>>> 
================== RESTART: /home/user/RTR105/skripts_12.py ==================
Enter hours:45
Enter rate:10
475
>>> 
================== RESTART: /home/user/RTR105/skripts_12.py ==================
Enter hours:45
Enter rate:10
475.0
>>> 
