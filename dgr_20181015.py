Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> if x < 10
SyntaxError: invalid syntax
>>> if x < 10:	print('Smaller')
if x > 20:	print('Bigger')
SyntaxError: invalid syntax
>>> if x < 10:
	print("Smaller")
if x > 20:
	
SyntaxError: invalid syntax
>>> if x < 10:
	print("Smaller")
x
SyntaxError: invalid syntax
>>> if x < 10:
	print("Smaller")

Smaller
>>> if x < 10:
	print("Smaller")
	if x > 20:	print("Bigger")
	print("Finis")

	
Smaller
Finis
>>> x = 87
>>> if x < 10:
	print("Smaller")
	if x > 20:	print("Bigger")
	print("Finis")

	
>>> if x < 10:
	print("Smaller")
	if x > 20:
	print("Bigger")
	print("Finis")
	
  File "<pyshell#19>", line 4
    print("Bigger")
        ^
IndentationError: expected an indented block
>>> if x < 10:
	print("Smaller")
	if x > 20:
	print("Bigger")
	
	print("Finis")
	
  File "<pyshell#20>", line 4
    print("Bigger")
        ^
IndentationError: expected an indented block
>>> if x < 10:
	print("Smaller")

if x > 20:
	print("Bigger")

	print("Finis")
	
SyntaxError: invalid syntax
>>> if x < 10:
	print("Smaller")

if x > 20:
	print("Bigger")

print("Finis")
SyntaxError: invalid syntax
>>> if x < 10:
	print("Smaller")

 if x > 20:
	print("Bigger")

print("Finis")
  File "<pyshell#23>", line 4
    if x > 20:
             ^
IndentationError: unindent does not match any outer indentation level
>>> if x < 10:
	print('Smaller')
	if x > 20:
		print("Bigger")

		
>>> if x < 10:
	print('Smaller')
	if x > 20:
		print("Bigger")
		print("Finis")

		
>>> if x < 10:
	print('Smaller')

	
	if x > 20:
		print("Bigger")
		print("Finis")

		
>>> x = 15
>>> if x < 10: print("Smaller")
if x > 12: print("Bigger")
SyntaxError: invalid syntax
>>> if x < 10: print("Smaller")if x > 12: print("Bigger")
SyntaxError: invalid syntax
>>> if x < 10:	print("Smaller")	if x > 12:	print("Bigger")
SyntaxError: invalid syntax
>>> if x < 10:	print("Smaller")if x > 12:	print("Bigger")
SyntaxError: invalid syntax
>>> if x < 10:print("Smaller")if x > 12:print("Bigger")
SyntaxError: invalid syntax
>>> x = 5
>>> if x == 5 :
	print('Equals 5')

	
Equals 5
>>> x >= 5 :
	
SyntaxError: invalid syntax
>>> if x >= 5 :
	print("Greater than or Equals 5")

	
Greater than or Equals 5
>>> if x >= 5 :
	print("Greater than or Equals 5")

Greater than or Equals 5
>>> x = 5
>>> 
KeyboardInterrupt
>>> x = 5
if x < 10:
    print("Smaller")
if x > 20:
    print("Bigger")
print("Finis")

>>> x = 5
>>> if x < 10:
    print("Smaller")
if x > 20:
    print("Bigger")
print("Finis")

SyntaxError: invalid syntax
>>> if x < 10:
    print("Smaller")
    if x > 20:
    print("Bigger")
    print("Finis")
    
  File "<pyshell#57>", line 4
    print("Bigger")
        ^
IndentationError: expected an indented block
>>> if x < 10:
    print("Smaller")
    if x > 20:
    print("Bigger")
print("Finis")
  File "<pyshell#58>", line 4
    print("Bigger")
        ^
IndentationError: expected an indented block
>>> x = 5
>>> if x > 2 :
	print("Bigger than 2")
	print("Still bigger")
    print("Done with 2")
    
  File "<pyshell#65>", line 4
    print("Done with 2")
                       ^
IndentationError: unindent does not match any outer indentation level
>>> if x > 2 :
	print("Bigger than 2")
	print("Still bigger")
print("Done with 2")
SyntaxError: invalid syntax
>>> if x > 2 :
	print("Bigger than 2")
	print("Still bigger")
print("Done with 2")
SyntaxError: invalid syntax
>>> if x > 2 :
	print("Bigger than 2")
	print("Still bigger")
print("Done with 2")
SyntaxError: invalid syntax
>>> if x > 2 :
	print("Bigger than 2")
	print("Still bigger")
	
print("Done with 2")
SyntaxError: invalid syntax
>>> if x > 2 :
	print("Bigger than 2")
	print("Still bigger")
print("Done with 2")
SyntaxError: invalid syntax
>>> if x > 2 :
	print("Bigger than 2")
	print("Still bigger")
print("Done with 2")
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)
	if i > 2:
		print("Bigger than 2")
	print("Done with i", i)
print("All Done")
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)
	if i > 2:
		print("Bigger than 2")
	print("Done with i", i)

	
0
('Done with i', 0)
1
('Done with i', 1)
2
('Done with i', 2)
3
Bigger than 2
('Done with i', 3)
4
Bigger than 2
('Done with i', 4)
>>> for i in range(5):
	print(i)
	if i > 2:
		print("Bigger than 2")
	print("Done with i", i)
	print("All Done")

	
0
('Done with i', 0)
All Done
1
('Done with i', 1)
All Done
2
('Done with i', 2)
All Done
3
Bigger than 2
('Done with i', 3)
All Done
4
Bigger than 2
('Done with i', 4)
All Done
>>> for i in range(5):
	print(i)
	if i > 2:
		print("Bigger than 2")
	print("Done with i", i)
print("All Done")
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)
	if i > 2:
		print("Bigger than 2")
	print("Done with i", i)
    print("All Done")
    
  File "<pyshell#87>", line 6
    print("All Done")
                    ^
IndentationError: unindent does not match any outer indentation level
>>> for i in range(5):
	print(i)
	if i > 2:
		print("Bigger than 2")
	print("Done with i", i)print("All Done")
	
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)
	if i > 2:
		print("Bigger than 2")
	print("Done with i", i)
    print("All Done")

	
  File "<pyshell#91>", line 6
    print("All Done")
                    ^
IndentationError: unindent does not match any outer indentation level
>>> for i in range(5):
	print(i)
	if i > 2:
		print("Bigger than 2")
	print("Done with i", i)
    print("All Done")
    
  File "<pyshell#92>", line 6
    print("All Done")
                    ^
IndentationError: unindent does not match any outer indentation level
>>> for i in range(5):
	print(i)
	if i > 2:
		print("Bigger than 2")
	print("Done with i", i)print("All Done")
	
SyntaxError: invalid syntax
>>> 
================== RESTART: /home/user/RTR105/skripts 1.py ==================
0
('Done with i', 0)
1
('Done with i', 1)
2
('Done with i', 2)
3
Bigger than 2
('Done with i', 3)
4
Bigger than 2
('Done with i', 4)
All Done
>>> 
================== RESTART: /home/user/RTR105/skripts_2.py ==================
more than one
Less than 100
All Done
>>> 
================== RESTART: /home/user/RTR105/skripts_3.py ==================
Bigger
All done
>>> 
================== RESTART: /home/user/RTR105/skripts_3.py ==================
Smaller
All done
>>> 
================== RESTART: /home/user/RTR105/skripts_3.py ==================
Small
Viss
>>> 
================== RESTART: /home/user/RTR105/skripts_4.py ==================
LARGE
Viss
>>> $ python3 notry.py
SyntaxError: invalid syntax
>>> $ cat notry.py
SyntaxError: invalid syntax
>>> astr = "Hello Bob"
>>> try:
	istr = int(astr)
    except:
	    
  File "<pyshell#99>", line 3
    except:
          ^
IndentationError: unindent does not match any outer indentation level
>>> 
================== RESTART: /home/user/RTR105/skripts_5.py ==================
('First', -1)
('Second', 123)
>>> 
================== RESTART: /home/user/RTR105/skripts_6.py ==================
Enter a number1
nice work
>>> 
================== RESTART: /home/user/RTR105/skripts_6.py ==================
Enter a number-4
Not a number
>>> 
================== RESTART: /home/user/RTR105/skripts_7.py ==================
Enter hours45

>>> 
================== RESTART: /home/user/RTR105/skripts_7.py ==================
Enter hoursded

Traceback (most recent call last):
  File "/home/user/RTR105/skripts_7.py", line 1, in <module>
    hrs = input("Enter hours")
  File "<string>", line 1, in <module>
NameError: name 'ded' is not defined
>>> exit()
>>> 
