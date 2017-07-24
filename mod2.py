Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> type (259+33)
<class 'int'>
>>> type (259-33.0)
<class 'float'>
>>> type (4)
<class 'int'>
>>> type ('4')
<class 'str'>
>>> type ('four')
<class 'str'>
>>> type (5/2.0)
<class 'float'>
>>> type (12>2*5)
<class 'bool'>
>>> type (color+3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type (color+3)
NameError: name 'color' is not defined
>>> type ('color'*4)
<class 'str'>
>>> my_name = 'student'
>>> print ("Hi," + myName')
       
SyntaxError: EOL while scanning string literal
>>> 
>>> my_name= 'student'
>>> print ("Hi," + myName')
       
SyntaxError: EOL while scanning string literal
>>> print ("Hi, student")
Hi, student
>>> print ('"Hi, student"')
"Hi, student"
>>> my_age = 15
>>> print ('I am' + my_age +'years old')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print ('I am' + my_age +'years old')
TypeError: Can't convert 'int' object to str implicitly
>>> print ('"I am 15 years old"')
"I am 15 years old"
>>> 
score=1
>>> score=1
>>> total=score+(count *2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    total=score+(count *2)
NameError: name 'count' is not defined
>>> score=1
>>> count=2
>>> total= score+(count*2)
>>> print(total)
5
>>> a=5
>>> b=10
>>> a=b
>>> b=a
>>> a
10
>>> b
10
>>> a=5
>>> b=10
>>> 1=b
SyntaxError: can't assign to literal
>>> a=b
>>> a
10
>>> b
10
>>> c=a
>>> a=b
>>> b=c
>>> a
10
>>> b
10
>>> four='4'
>>> a=5
>>> b=10
>>> a=b
>>> a
10
>>> b
10
>>> b=a
>>> a
10
>>> b
10
>>> four='4'
>>> print(four*3)
444
>>> five=4
>>> print(five)
4
>>> print(five*3)
12
>>> my_name+'student'
'studentstudent'
>>> my_name='student'
>>> print("My name is'+'my_name")
My name is'+'my_name
>>> print("My name is"+ my_name)
My name isstudent
>>> print("My name is" + my_name)
My name isstudent
>>> my_name = 'student'
>>> print('My name is" + my_name)
      
SyntaxError: EOL while scanning string literal
>>> print("My name is" + my_name)
My name isstudent
>>> my_name= 'student'
>>> print("Hi," + myName)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print("Hi," + myName)
NameError: name 'myName' is not defined
>>> my_name= 'student'
>>> print("Hi," + my_name)
Hi,student
>>> print('"Hi," + my_name"')
"Hi," + my_name"
>>> my_age= 15
>>> print('I am '+my_age+ 'years old')
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print('I am '+my_age+ 'years old')
TypeError: Can't convert 'int' object to str implicitly
>>> print('I am' + 'my_age' + 'years old')
I ammy_ageyears old
>>> my_age= '15'
>>> print('I am' + 'my_age' +'years old')
I ammy_ageyears old
>>> print("i am"+ my_age + "years old")
i am15years old
>>> score=1
>>> total=score+ (count*2)
>>> print(total)
5
>>> 
