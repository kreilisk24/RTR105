Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> name = raw_input("Enter:")
Enter:Chuck
>>> print(name)
Chuck
>>> apple = input("Enter")
Enter100
>>> x = apple - 10
>>> x = int(apple) - 10
>>> print(x)
90
>>> fruit = "banana"
>>> letter = fruit[1]
>>> print(letter)
a
>>> x =3
>>> w = fruit[x-1]
>>> print(w)
n
>>> print(len(fruit))
6
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index + 1

	
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
>>> for letter in fruit:
	print(letter)

	
b
a
n
a
n
a
>>> word = "banana"
>>> count = 0
>>> for letter in word:
	if letter == "a":
		count = count + 1

		
>>> print(count)
3
>>> s = "Monty Python"
>>> print(s[0:4])
Mont
>>> print(s[6:7])
P
>>> print(s[6:20])
Python
>>> print(s[:3])
Mon
>>> print(s[4:])
y Python
>>> print(s[:])
Monty Python
>>> a = "hello"
>>> b = a + "there"
>>> print(b)
hellothere
>>> c = a +" "+"there"
>>> print(c)
hello there
>>> fruit = "banana"
>>> "n" in fruit
True
>>> "m" in fruit
False
>>> "nan" in fruit
True
>>> if "a" in fruit:
	print("Found it")

	
Found it
>>> if word == "banana":
	print("All right, bananas.")

	
All right, bananas.
>>> if word < "banana":
	print("Whazzza," + word +", comes before banana.")
elif word > "banana":
	print("Whazza,"+ word +", comes after banana")
else:
	print("All right, bannana.")

	
All right, bannana.
>>> greet = "Hello Bob"
>>> zap = greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
>>> print("Hi THERE".lower())
hi there
>>> stuff = "Hello world"
>>> type(stuff)
<type 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str.rpartition(sep)

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    str.rpartition(sep)
NameError: name 'sep' is not defined
>>> sep = "Great Britain"
>>> str.rpartition(sep)

Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    str.rpartition(sep)
TypeError: rpartition() takes exactly one argument (0 given)
>>> sep = "alpha"
>>> str.rpartition(sep)

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    str.rpartition(sep)
TypeError: rpartition() takes exactly one argument (0 given)
>>> print("alpha".rpartition())

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print("alpha".rpartition())
TypeError: rpartition() takes exactly one argument (0 given)
>>> print("a".rpartition())

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print("a".rpartition())
TypeError: rpartition() takes exactly one argument (0 given)
>>> print(a.rpartition())

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    print(a.rpartition())
TypeError: rpartition() takes exactly one argument (0 given)
>>> a = 5
>>> print(a.rpartition())

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print(a.rpartition())
AttributeError: 'int' object has no attribute 'rpartition'
>>> fruit = "banana"
>>> pos = fruit.find("na")
>>> print(pos)
2
>>> greet ="Hell Bob"
>>> nstr = greet.replace("Bob","Jane")
>>> print(nstr)
Hell Jane
>>> stuff.casefold()

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    stuff.casefold()
AttributeError: 'str' object has no attribute 'casefold'
>>> a.casefold()

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.casefold()
AttributeError: 'int' object has no attribute 'casefold'
>>> aa.casefold.__doc__

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    aa.casefold.__doc__
NameError: name 'aa' is not defined
>>> a.casefold.__doc__

Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.casefold.__doc__
AttributeError: 'int' object has no attribute 'casefold'
>>> fruit.center()

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    fruit.center()
TypeError: center() takes at least 1 argument (0 given)
>>> fruit.center("n")

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    fruit.center("n")
TypeError: an integer is required
>>> fruit.center(4)
'banana'
>>> fruit.center(19)
'       banana      '
>>> greet = "      Hello   Bob    "
>>> greet.lstrip()
'Hello   Bob    '
>>> greet.rstrip()
'      Hello   Bob'
>>> greet.strip()
'Hello   Bob'
>>> line = "please have a nice day"
>>> line.startswith("Please")
False
>>> line.startswith("please")
True
>>> line.startswith("p")
True
>>> data = "From stephen.margard@uct.ac.za Jan 5 09;:14:16 2018
SyntaxError: EOL while scanning string literal
>>> data = "From stephen.margard@uct.ac.za Jan 5 09;:14:16 2018"
>>> atpos = data.find("a")
>>> print(atpos)
14
>>> sppos = data.find(" ",atpos)
>>> print(sppos)
30
>>> host = data[atpos+1 : sppos]
>>> print(host)
rgard@uct.ac.za
>>> 
