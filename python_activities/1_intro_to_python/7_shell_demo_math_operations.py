"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""
Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = 5
>>> c = 2
>>> d = 3
>>> sum_a_b = a + b
>>> sum_a_b
15
>>> a-d
7
>>> b*2
10
>>> c/2
1.0
>>> bedmas = (a+b)-a/c*d
>>> bedmas
0.0
>>> abs(-45) #absolute function
45
>>> abs(-10) #absolute function
10
>>> 2**2 #exponents
4
>>> 2**3 #exponents
8
>>> 2**4 #exponents
16
>>> 25**1/2 #square root wrong
12.5
>>> 25**(1/2) #square root correct (BEDMAS)
5.0
>>> import math #import the math library to really advance stuff
>>> math.sqrt(25) #square root
5.0
>>> math.sqrt(17) #square root
4.123105625617661
>>> math.sin(45) #sin...but result is weird
0.8509035245341184
>>> math.sin(90) #what is going on?
0.8939966636005579
>>> angle_rad = math.radians(90) #math trig functions accepts radians so we have to convert degrees to radians
>>> angle_rad
1.5707963267948966
>>> math.sin(angle_rad)#sin...thats more like it
1.0
>>> math.cos(angle_rad) #sin...result is basically 0
6.123233995736766e-17
>>> angle_rad = math.radians(45) #change 45 degrees
>>> math.sin(angle_rad)
0.7071067811865475
>>> math.cos(angle_rad)
0.7071067811865476
>>> math.tan(angle_rad) #tan...result is basically 1
0.9999999999999999
>>> 
