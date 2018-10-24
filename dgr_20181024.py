Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /home/user/RTR105/skripts_22.py ==================
Leather
rinse
Leather
rinse
Leather
rinse
Leather
rinse
Leather
rinse
Dry off
>>> 
================== RESTART: /home/user/RTR105/skripts_22.py ==================
>hello there

Traceback (most recent call last):
  File "/home/user/RTR105/skripts_22.py", line 2, in <module>
    line = input(">")
  File "<string>", line 1
    hello there
              ^
SyntaxError: unexpected EOF while parsing
>>> 
================== RESTART: /home/user/RTR105/skripts_22.py ==================
> hello there

Traceback (most recent call last):
  File "/home/user/RTR105/skripts_22.py", line 2, in <module>
    line = input("> ")
  File "<string>", line 1
    hello there
              ^
SyntaxError: unexpected EOF while parsing
>>> 
================== RESTART: /home/user/RTR105/skripts_22.py ==================
> hello there
hello there
> finished
finished
> comp
comp
> line
line
> done
Done
>>> 
================== RESTART: /home/user/RTR105/skripts_23.py ==================
>holla
holla
># dont print this
>print this!
print this!
>done
Done
>>> 
================== RESTART: /home/user/RTR105/skripts_23.py ==================
> #
 #
>#
>Ok
Ok
>done
Done
>>> 
================== RESTART: /home/user/RTR105/skripts_24.py ==================
5
4
3
2
1
Blastoff
>>> 
================== RESTART: /home/user/RTR105/skripts_25.py ==================
('Happy New Year:', 'Joseph')
('Happy New Year:', 'Glenn')
('Happy New Year:', 'Arnold')
done!
>>> 
================== RESTART: /home/user/RTR105/skripts_26.py ==================
('Before', -1)
(9, 9)
(41, 41)
(41, 12)
(41, 3)
(74, 74)
(74, 15)
('After', 74)
>>> 
================== RESTART: /home/user/RTR105/skripts_27.py ==================
('Before', 0)
(9, 9)
(50, 41)
(62, 12)
(65, 3)
(139, 74)
(154, 15)
('after', 154)
>>> 
================== RESTART: /home/user/RTR105/skripts_28.py ==================
Before
('Large number', 419)
('Large number', 1299)
('Large number', 39)
('Large number', 74)
After
>>> 
============= RESTART: /home/user/RTR105/skripts_true_meklet.py =============
('Before', False)
(False, 9)
(False, 41)
(False, 12)
(True, 3)
(True, 74)
(True, 15)
('After', True)
>>> 
================== RESTART: /home/user/RTR105/skripts_is.py ==================
Before
(3, 3)
(3, 31)
(3, 12)
(3, 9)
(3, 74)
(3, 15)
('After', 3)
>>> 
================ RESTART: /home/user/RTR105/skripts_isnot.py ================
Before
(None, 3)
(None, 31)
(None, 12)
(None, 9)
(None, 74)
(None, 15)
('After', None)
>>> 
================ RESTART: /home/user/RTR105/skripts_isnot.py ================
Before
(None, 3)
(None, 31)
(None, 12)
(None, 9)
(None, 74)
(None, 15)
('After', None)
>>> 
================ RESTART: /home/user/RTR105/skripts_isnot.py ================
Before
(None, 3)
(None, 31)
(None, 12)
(None, 9)
(None, 74)
(None, 15)
('After', None)
>>> 
================ RESTART: /home/user/RTR105/skripts_isnot.py ================
Before
(3, 3)
(31, 31)
(12, 12)
(9, 9)
(9, 74)
(9, 15)
('After', 9)
>>> 
============ RESTART: /home/user/RTR105/skripts_count_average.py ============
('before', 0, 0)
(1, 9, 9)
(2, 50, 41)
(3, 62, 12)
(4, 65, 3)
(5, 139, 74)
(6, 154, 15)
('after', 6, 154, 25.666666666666668)
>>> 
=================== RESTART: /home/user/RTR105/print_%.py ===================

Traceback (most recent call last):
  File "/home/user/RTR105/print_%.py", line 1, in <module>
    print("%s %s %f" %(one, two, three))
NameError: name 'one' is not defined
>>> 
=================== RESTART: /home/user/RTR105/print_%.py ===================

Traceback (most recent call last):
  File "/home/user/RTR105/print_%.py", line 1, in <module>
    print("%s %s %f" %("one", "two", "three"))
TypeError: float argument required, not str
>>> 
=================== RESTART: /home/user/RTR105/print_%.py ===================

Traceback (most recent call last):
  File "/home/user/RTR105/print_%.py", line 1, in <module>
    print("%s %s %f" %("one", "two", "3"))
TypeError: float argument required, not str
>>> 
=================== RESTART: /home/user/RTR105/print_%.py ===================
one two 3.000000
>>> 
==================== RESTART: /home/user/RTR105/test1.py ====================
number please:56
>>> 
==================== RESTART: /home/user/RTR105/test1.py ====================
number please:56
OK
>>> 
==================== RESTART: /home/user/RTR105/test1.py ====================
number please:lol

Traceback (most recent call last):
  File "/home/user/RTR105/test1.py", line 1, in <module>
    rawstr = input("number please:")
  File "<string>", line 1, in <module>
NameError: name 'lol' is not defined
>>> 
==================== RESTART: /home/user/RTR105/test1.py ====================
number please:-1
Invalid
>>> 
==================== RESTART: /home/user/RTR105/test1.py ====================
number please:ll

Traceback (most recent call last):
  File "/home/user/RTR105/test1.py", line 1, in <module>
    rawstr = input("number please:")
  File "<string>", line 1, in <module>
NameError: name 'll' is not defined
>>> 
==================== RESTART: /home/user/RTR105/test1.py ====================
>>> 
number please:rt

Traceback (most recent call last):
  File "/home/user/RTR105/test1.py", line 2, in <module>
    rawstr = input("number please:")
  File "<string>", line 1, in <module>
NameError: name 'rt' is not defined
>>> 
