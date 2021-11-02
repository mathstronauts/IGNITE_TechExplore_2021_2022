"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""

Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# SyntaxError: most common error, occurs when a statement does not follow its usual usage
>>> print "hello world"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello world")?
>>>
>>>
# IndexError: occurs when tryign to access an item at an index position that does not exist
>>> L1 = [1, 2, 3, 4]
>>> L1[5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    L1[5]
IndexError: list index out of range
>>> 
>>> 
# ModuleNotFoundError: occurs when a python library cannot be found on the computer
>>> import notamodule
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    import notamodule
ModuleNotFoundError: No module named 'notamodule'
>>>
>>>
# Key Error: occurs when a key in a dictionary is not found
>>> D1 = {"A": "values", "B": 1, "C": True}
>>> D1["D"]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    D1["D"]
KeyError: 'D'
>>>
>>>
# ImportError: occurs when a specified function cannot be found
>>> from math import cube
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    from math import cube
ImportError: cannot import name 'cube' from 'math' (unknown location)
>>>
>>>
# TypeError: occurs when the incorrect datatype is used
>>> 2+2
4
>>> "2" + 2
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    "2" + 2
TypeError: can only concatenate str (not "int") to str
>>>
>>>
# ValueError: occurs when a function's argument is the incorrect datatype
>>> int("9")
9
>>> int("abc")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int("abc")
ValueError: invalid literal for int() with base 10: 'abc'
>>>
>>>
# NameError: occurs when an object could not be found - usually when you did not define the variable you are using
>>> name = "Nancy"
>>> name
'Nancy'
>>> age
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    age
NameError: name 'age' is not defined
>>>
>>>
# ZeroDivisionError: occurs when the second operator in a division operation is zero, you cannot divide by zero in python
>>> num = 100 / 0
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    num = 100 / 0
ZeroDivisionError: division by zero
>>> 
>>> 
>>> # Those are the main errors you may encounter in python!
