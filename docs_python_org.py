#https://realpython.com/setting-up-sublime-text-3-for-full-stack-python-development/
#http://pythontutor.com/visualize.html#mode=display                               *********Best way to understand
#https://www.udemy.com/pythonautomation/   check this course
#https://github.com/codingforentrepreneurs/30-Days-of-Python
#https://www.pythonforbeginners.com/games/
#http://pythontutor.com/
#Virtual environments
# Python programs can be stopped at any time by pressing Ctrl-C (on Windows) or Ctrl-D (on Mac and Linux)

#comment
#( ''' or """ ) this is called Docstring

#Vertual enviroment for specific project
>>>python -m venv my-project
>>>source my-project/bin/activate
>>>pip install all-the-modules 

#install package from .whl file
>>>pip install C:/some-dir/some-file.whl        #some-file.whl is a file in some location in computer      


>>> print((1, 2) + (3, 4))
(1, 2, 3, 4)

>>> print(1,000,000)
1 0 0   

>>>print(1_000_000)
1000000

>>>print(000000000)
0

>>> 02+02
  File "<stdin>", line 1
    02+02
     ^
SyntaxError: invalid token
>>> 2+02
  File "<stdin>", line 1
    2+02
       ^
SyntaxError: invalid token
>>> 202
202
>>> 2 3
  File "<stdin>", line 1
    2 3
      ^
SyntaxError: invalid syntax

>>>42 = n
  File "<stdin>", line 1
SyntaxError: can't assign to literal                                                                                                        


#printing 3 different values
>>> print('Hi', 'hello world', 'bye bye')
Hi hello world bye bye

#New line with print function
>>>s = 'First line.\nSecond line.'                      # \n means newline
>>>s                                                    # without print(), \n is included in the output
'First line.\nSecond line.'

>>> print(s)                                          # with print(), \n produces a new line
First line.
Second line.

>>> print('C:some\name')                      # here \n means newline!
C:some
ame

>>>len(s)              #Inbuild length function for the string length
24


>>> 'Py' 'thon' #Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
'Python'

>>>"hi how are you" + " Gautam"               #Merge two string on shell
 'hi how are you Gautam'

>>> 2++2
4
>>> 2--2
4

# exponentiation; that is, it raises a number to a power:
>>> 6**2 + 6
42

# ^ is used for exponentiation, but in Python it is a bitwise operator called XOR
>>> 6 ^ 2
4


>>> x=y=1
>>> y
1

>>> x, y = 1, 2
>>> y
2
>>> x
1

>>>y = 100 < 10
>>>y
False

>>> True == 1
True
>>> False == 0
True
>>> 

a, b, c = 5, 3.2, "Hello"

print (a)  --> 5
print (b)  --> 3.2
print (c) --> Hellos

x = y = z = "same"

print (x) -->same
print (y) -->same
print (z) -->same


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Format !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# .format can be used to format strings, like this:
"{} can be {}".format("Strings", "interpolated")             # => "Strings can be interpolated"
-->'Strings can be interpolated'

# You can use keywords if you don't want to count.
"{name} wants to eat {food}".format(name="Bob", food="lasagna")  
-->"Bob wants to eat lasagna"

#The String format() Method
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))    
We are the knights who say "Ni!"

>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Sleep for a 30 seconds
import time
print("Sleeping")
time.sleep(30)                    # sleep for a while; interrupt me!
print("Done Sleeping")

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#id of a variable
>>>a=10
>>>print(id(a))  #We can get the address (in RAM) of some object through this id() function.

--> 1582487872

#Using underscore
a,_ = (1,2)   #to telll interpreter we use just here variable skip

print(a)

print("##############")

#Using unpacking more lenght variables
a,b,*c = (1,2,3,4,5,67,7,87,3)

#unpack
print(a)
print(b)
print(c)     #It will contain remaining all

print("##############")

a,b,*_,d = (1,2,3,4,5,6,7,8,9)

print(a)
print(b)
#print(c)     
print(d)


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! INPUT FUNCTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Input function (By default python Interpreter takes input as a string)
a=input('Eter first No:')
b=input('Enter Second No:')
c=a+b
print(c)

--> Eter first No:2
--> Eter Second No:3
-->23                       #because its add 2 or 3 as a string

#Typecaste inpute as a integer to add in mathematical calculation
a=int(input('Eter first No:'))
b=int(input('Enter Second No:'))
c=a+b
print(c)

--> Eter first No:2
--> Eter Second No:3
-->5                       #Now it will add 2&3 and return 5


#passing index value in charactor syntex
ch = input('Enter a char:')[0]
print(ch)

-->Enter a char:gjjhh
-->g

#Eval function(evaluate a function)
result = eval(input('Enter a Expression:'))
print(result)

-->Enter a Expression:5+9+6-4
-->16

#taking inpute as a aruguments
#***Run as python test.py 23 22
import sys

a = int(sys.argv[1])         #pass 1 because at index 0 filename.py
b = int(sys.argv[2])         #pass 2 because at index 1 first no  
c=a+b
print(c)

-->45

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#The simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables.
>>> s = 'Don'
>>> s
'Don'
>>> a, b, c = s # Unpack into variables
>>> a
'D'
>>> b
'o'
>>> c
'n'

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#If you are not sure what type a value has, the interpreter can tell you
>>>type(y)
bool

>>> type(17)
<class 'int'>

>>> type(3.2)
<class 'float'>

>>> type('2')
<class 'str'>


>>>x, y = 1, 2
>>>x < y
True
>>>x > y
False

>>>x = 1    # Assignment
>>>x == 2   # Comparison
False

>>>1 != 2         #For “not equal” use !=
True

>>>print(True==True)
True

>>>print(True!=True)
False

>>>print(not True is True)
False
>>>print(not True is not True)
True

>>>print(100-32 == 68)
True

>>>print(10**2 is 100)
True

# Note "and" and "or" are case-sensitive
True and False  # => False
False or True   # => True

#Type conversion functions
#To int
>>> int(3.99999)
3
>>> int(-2.3)
-2

#float converts integers
>>> float(32)
32.0
>>> float('3.14159')
3.14159

#str converts its argument to a string
>>> str(32)
'32'
>>> str(3.14159)
'3.14159'

#concatenate variables 
>>>prefix = 'Py'
>>>prefix + 'thon'              #Now prefix hold the 'py' string
'Python'

#2 upper method
var = "Hello, John"
print(type(var)) # ‘str’> or <class 'str'>
print(var.upper()) # upper() method is called, HELLO, JOHN

# lower method
>>> str = 'WOAH!'
>>> str.lower()
-->'woah!'

#replace() allows you to replace any character with another character.
>>> str = 'rule'
>>> str.replace('r', 'm')
-->'mule'

#count() lets you know how many times a certain character appears in the string.
>>> number_list =['one', 'two', 'one', 'two', 'two']
>>> number_list.count('two')
-->3

#The in Operator
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False


#interactive operator"_"
>>>1+8
9
>>>_                  #it is reference to the output of the last executed expresssion
9
>>>prin(_)

#_____________________#
#The sep separator is used between the values. It defaults into a space character.
#After all values are printed, end is printed.
>>>print(1, 2, 3, sep=' < ')
1 < 2 < 3

>>>print(1, 2, 3, sep=' , ')
1 , 2 , 3

>>>print(1, 2, 3,sep='\n')
1
2
3

#_____________________#
#Docstring in Python
def double(num):
    """Function to double the value"""
    return 2*num

double(5)                    # this will return   10
print(double.__doc__)      # this will return --> Function to double the value

#_____________________#
#Adding optional arguments with default values to the functions we define
def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")

#_____________________#
#chr() in Python
#The chr() method returns a string representing a character whose Unicode code point is an integer.
#The chr() method takes only one integer as argument.
print(chr(71), chr(97), chr(117), chr(116), chr(97), chr(109)) 
 
 
#Accepting password on command line
from getpass import getpass
username = input('Username: ')
password = getpass('password: ')         #it will hide text while taking input from keyboard

print("Logging In....") 

#How slices Work
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DATES !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
--> datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

#The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,


# dates support calendar arithmetic
>>>from datetime import date
>>> birthday = date(1993, 10, 26)
>>> now = date.today()
>>> age = now - birthday
>>> age.days
14368

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#system Info
import sys
print(sys.version_info)
print(sys.version)


#clear Screen in window
>>>import os
>>>os.system("cls")

#built in function for max
>>> max('Hello world')
'w'                                      #“largest character” in the string
#built in function for min
>>> min('Hello world')
' '                                      #smallest character
>>>

#create a folder
import os
os.mkdir("New folder")                  # create a folder new folder

#create multiple folders
import os
folders = ['folder1','folder2','folder3','folder4']
for x in folders:
   os.mkdir(x)

#Create tree structure folder
>>>from os import makedirs
>>>makedirs('1/2/3/4/5/6/7/8/9/1/1/2/3/3/4/4/5/65/6/6/6/7/7/88/8/9/2/23/2/3/5/6/8/9//5/4/3/2/2//1/3/5/6/6/778/88/2/3/4/5/')   

#print Table of any no
no = int(input("Enter a no for a table:"))
for x in range(1,11):
  print(x*no)

#range function
>>>list(range(5))
[0, 1, 2, 3, 4]

#print numbers
for x in range(1,100,4):   #print no between 1 to 100 and gap betwwen 4 (it will print no between gap of 4 from 1 to 100)
  print(x)

#with delimiter
for x in range(1,30,2):
  print(x,"/",end="")      #print with / betwwen no

#To know path in python shell where you are
>>>import os
>>>os.getcwd()

#change directory
>>>os.chdir('my_path')

#to check any directory exist on current location or not
>>>os.path.isdir('music')

#Mouse position
>>>import pyautogui
>>>pyautogui.position()

#click
pyautogui.click(10, 5)

#locateOnScreen, a pyautogui method to locate the extension' x & y coordinates in screen
v = pyautogui.locateOnScreen("E:\\python\\New 11022019\\Click chrome extention\\findicon.PNG") ##save the extension as image

#trigger click event using the pyutogui click method on perticular location
>>>import pyautogui
>>>pyautogui.click(x=v[1267],y=v[49],clicks=1,interval=0.0,button="left")

#swap the no
>>>x, y = 10, 20
>>>print(x, y) 
>>>x, y = y, x 
>>>print(x, y)

#Enumerate
#The enumerate () method adds a counter to an iterable and returns the enumerate object.

>>>names = ['Rajesh', 'Rahul', 'Aarav', 'Sahil', 'Trevor']
>>>enumerate(names)
<enumerate object at 0x031D9F80>
>>>list(enumerate(names))
[(0, 'Rajesh'), (1, 'Rahul'), (2, 'Aarav'), (3, 'Sahil'), (4, 'Trevor')]


#Random numbers
import random
for i in range(10):
	x = random.random()

print(x)

#random number between range
>>> random.randint(5, 10)
5
>>> random.randint(5, 10)
9

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! STRING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#String strip() Function --> remove unwanted characters from either the beginning or ending of a string. 
#To strip whitespace (spaces, tabs, newline characters, etc).

>>> orig_text = '     The cow jumped over the moon!        \n'
>>> print(orig_text.strip())
The cow jumped over the moon!  

#Specify the strip charactor
>>> orig_text = '-----The cow jumped over the moon!$$$$$'
>>> print(orig_text.strip('-$'))
The cow jumped over the moon!

#strip characters from only one side of the string via the String.rstrip() and String.lstrip() methods.
>>> orig_text = '*****The cow jumped over the moon!*****'
>>> print(orig_text.rstrip('*'))
*****The cow jumped over the moon!
>>> print(orig_text.lstrip('*'))
The cow jumped over the moon!***** 

#______________________________________#
# The in Operator
fullstring = "StackAbuse"  
substring = "tack"

if substring in fullstring:  
    print("Found!")
else:  
    print("Not found!")
    


#Reverse String
>>>a ="GeeksForGeeks"
>>>print("Reverse is", a[::-1])

#Create a single string from all the elements in list Using "join" function
>>>a = ["Geeks", "For", "Geeks"] 
>>>print(" ".join(a))
--> Geeks For Geeks

#to .join() for string
>>>print(":".join("Python"))
-->P:y:t:h:o:n

#Reversing String 
>>>string="12345"    
>>>print(''.join(reversed(string)))
-->54321

#Split Strings
>>>word="guru99 career guru99"   
>>>print(word.split(' '))
--->['guru99', 'career', 'guru99']

#Split string on base of some charactor
>>>word="guru99 career guru99"   
>>>print(word.split('r'))
-->['gu', 'u99 ca', 'ee', ' gu', 'u99']

#String to charactor
>>>for x in "PYTHON":

   print(x)
   print(end=' ')
   print(x*3)

#Count Vowel in the String
string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels) 


#function call
def greet(first_name, last_name):
  print(first_name +' '+ last_name)
  
greet("Lionel", "Messi")


#Print The File Path Of Imported Modules
>>>import os; 
>>>import socket; 
  
>>>print(os)                     #it will print os module file path
>>>print(socket)                 #it will print socket module file path

#Store all values of List in new separate variables
a = [1, 2, 3] 
x, y, z = a  
print(x) 
print(y) 
print(z)  

# declare multiline variable/operation
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a) 
45

# declare multiline variable/operation
a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)   

print(a)
45

#ZIP (dictionary out of two lists)
>>>keys = ['a', 'b', 'c']
>>>vals = [1, 2, 3]
>>>zipped = dict(zip(keys, vals))

#Universally Unique IDs (or ‘UUIDs’)
#there are over 2¹²² possible UUIDs that can be generated
>>>import uuid
>>>user_id = uuid.uuid4()
>>>print(user_id)

#printing out any large, nested object(complex structured objects in an easy-to-read format)
import pprint
url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()
pprint.pprint(users)

#Adding breakpoint in code we can add it anywhere in code
import pdb     #module for it

pdb.set_trace()       #add this on anywhere in code to set breakpoint on  that place


#_________________________________________________________________________________#
#Emoji
from emoji import emojize
print(emojize(":thumbs_up:"))
#_________________________________________________________________________________#
# Shallow and deep copy
# Shallow copy: Shallow copy creates a new object and then use the reference to refer the inner objects. 
>>> a = [[1,2],[3,4]]
>>> b = a.copy()
>>> print(id(a) == id(b))
False
>>> print(id(a[0]) == id(b[0]))
True

# Deep copy: deep copy create a new object and recursively copy the inner objects too. 
>>> from copy import deepcopy
>>> a = [[1,2],[3,4]]
>>> b = deepcopy(a)
>>> print(id(a) == id(b))
False
>>> print(id(a[0]) == id(b[0]))
False

#_________________________________________________________________________________#
#capetize words
>>>import string
>>>text = 'Tutorialspoint - simple easy learning.'
>>>print(string.capwords(text))
Tutorialspoint - Simple Easy Learning.

#Word Replacement
>>>str = "this is string example....wow!!! this is really string"
>>>print(str.replace("is", "was"))                                       #Old text New text
>>>print(str.replace("is", "was", 3))                                    # Max
thwas was string example....wow!!! thwas was really string
thwas was string example....wow!!! thwas is really string


#________________________________________________________________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Module!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#A Python module is a package to encapsulate reusable code.
#Modules contain functions and classes.
#Modules are imported using the import keyword
#Import Module
#Now, you can access the functions or variables in that module with the ‘.’ (dot) Operator.

# prints a list of existing modules
>>>print(help('modules'))

>>>import smtpd
>>>help(smtpd)              #show help on smtpd

#Reading Module Documentation
>>>import os
>>>print(help(os))                              # print the module's online manual
>>>print(help(list))                            # print the module's online manual
>>>print(dir(re))                               #List Module's Function/Variable Names

#calc module(save it as calc.py in same location)
def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b  

#using this module
from calc import *            # to use all calc funcction(1st case)
from calc import sub          #use only sub function(2nd case)

a =7
b=18

#first case
a= add(a,b)  
print(a)    

#second case
a = calc.sub(a,b)
print(a)


#__________________________________________________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Conditional execution !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if x > 0 :
  print('x is positive')

if x < 0 :
  pass # need to handle negative values!

#Alternative execution
if x%2 == 0 :
  print('x is even')
else :
  print('x is odd')

#Chained conditionals
if x < y:
  print('x is less than y')
elif x > y:                              #elif is an abbreviation of “else if.”
  print('x is greater than y')
else:
  print('x and y are equal')

#Nested conditiona
if x == y:
  print('x and y are equal')
else:
  if x < y:
    print('x is less than y')
  else:
    print('x is greater than y'

#2 nested Condition

if 0 < x:
  if x < 10:
    print('x is a positive single-digit number.'



#A Python 'if not' operator
x = 10
if not x > 10:
    print("not retured True")
else:
    print("not retured False")


#_________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! List !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

>>>[]
[]

>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')                                                        #Return the number of times apple appears in the list
2
>>> fruits.index('banana')                  # Find index of banana 
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()                  #Reverse the elements of the list in place. 
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')                                         #AAppends object at the end.
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()                                                               #Sort Elements alphabetically
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']       
>>> fruits.pop()                                                                          #pop(remove) the last element
'pear'
>>>fruits.pop(1)                                                       #remove 1 index element
'apple'
>>> fruits.clear()                                                    #remove all element from Equivalent to del a[:]
>>> fruits
[]
>>>fruits.copy()                                 #coppy the list

# special syntax for the stride of a slice in the form somelist[start:end:stride].(stride syntex)
>>>a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
>>>odds = a[::2]
>>>evens = a[1::2]                         #select every second item starting at the beginning
>>>print(odds)
['red', 'yellow', 'blue']
>>>print(evens)
['orange', 'green', 'purple']
>>>print(a[::-2])                             #select every second item starting at the end and moving backwards
['purple', 'green', 'orange']

>>>a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
>>>a[2::2]                
['c', 'e', 'g']
>>>a[-2::-2]           
['g', 'e', 'c', 'a']
>>>a[-2:2:-2] 
['g', 'e']
>>>a[2:2:-2] 
[]
>>>b = a[::2] 
['a', 'c', 'e', 'g']
>>>c = b[1:-1] 
['c', 'e']

>>> l = [10, 20, 30, 40, 50, 60]
>>> l[:2] # split at 2
[10, 20]
>>> l[2:]
[30, 40, 50, 60]

#slicing object
>>> s = 'bicycle'
>>> s[::3]
'bye'
>>> s[::-1]
'elcycib'
>>> s[::-2]
'eccb'

#_____________________________________________________________#
# append() vs extend()
# append()  --> method adds a single item to the end of the list
x = [1, 2, 3]
x.append([4, 5])
x.append('abc')
print(x)
# gives you
[1, 2, 3, [4, 5], 'abc']

# extend() --> method takes one argument, a list, and appends each of the items of the argument to the original list
x = [1, 2, 3]
x.extend([4, 5])
x.extend('abc')
print(x)
# gives you
[1, 2, 3, 4, 5, 'a', 'b', 'c']

#_____________________________________________________________#

#using variable for index
>>>list_n=['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>>x=0
>>>list_n[x]
'banana'
>>>list_n[x+1]
'apple'

#adding list by sum function
>>> list=[6,7,8,9]
>>> total=sum(list)
>>> total
30
>>>average=total/len(list)       #for find average
>>>average
7.5


#The del statement
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]

#Copy list to another variable
>>> a = [1, 2, 3]
>>> b = a
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]
>>> a.append(4)
>>> b
[1, 2, 3, 4]
>>> a == b
True
>>> a is b
True
>>> c = list(a)               #identical copy of our list object.
>>> c
[1, 2, 3]
>>> a == c
True
>>> a is c
False        #Boom! This is where we get a different result. Python is telling us that c and a are pointing to two different objects, even though their contents might be the same.

#________________________________________________________ List Comprehensions ______________________________________________#
# Syntex for List Comprehension
"""
new_list = [ expression for element in old_list if condition]
new_list    
The resulting list.
expression
The operation performed whenever an element fulfills the given condition, like i**3 in previous example. The result of this expression is stored in new_list.
for element in old_list
Iterates over each element in old_list
if condition
Apply a condition using an If-statement.
"""

# Suppose you wish to find cube of all numbers in a list and store them in a new list. Using a for loop, we can code this as follows:
list = [1, 2, 3, 4]
cube_list = []

for i in list:
  cube_list.append(i**3) 

print(cube_list)  #  Output: [1, 8, 27, 64]

#using List Comprehension
list = [1, 2, 3, 4]
cube_list = [i**3 for i in list]

print(cube_list) # Output: [1, 8, 27, 64]

list = [1, 2, 3, 4]
new_list = [i**3 if i%2 == 0 else i**2 for i in list]

print(new_list) # Output: [1, 8, 9, 64]

#______________________________________#

#List Comprehensions to create a list from -5 to 5 range
>>>b = [value for value in range(-5,5)]
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]



#List Comprehensions
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>>list=[1,2,3]
>>>for i in list:
   print(i)
 1
 2
 3

>>>for i in list:
   print(i*2)
 1
 4
 9

#__________________________________#
# isinstance() -->The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo 
                 #class (second argument).

#The isinstance() takes two parameters:
      # object - object to be checked
      # classinfo - class, type, or tuple of classes and types

#seprate integer and string from a list of string and integers
items = ["Mic", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 134]

str_items = []
num_items = []

for i in items:
    
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass

print(str_items)
# output --> ['Mic', 'Phone', 'Justin', 'Bag', 'Cliff Bars']

print(num_items)
# output --> [323.12, 3123.123, 134]

#__________________________________#
#this listcomp combines the elements of two lists if they are not equal
>>>a= [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
>>>a
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

#create List 
>>> vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]

# filter the list to exclude positive numbers
>>> [x for x in vec if x <= 0]
[-4,-2, 0]

# apply a function to abs the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]

# create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(8)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]                        #num,elem is variable it can be changed
[1, 2, 3, 4, 5, 6, 7, 8, 9]

#Even Sqaures
>>> even_squares = [x * x for x in range(10) if not x % 2]
>>> even_squares
[0, 4, 16, 36, 64]


#List comprehensions can contain complex expressions and nested functions:
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']

#Passing an integer after the ':' will cause that field to be a minimum number of characters wide
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')

Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678


#A tidily-aligned set of columns giving integers and their squares and cubes:
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

#Using object
stuff = list()                   #constructs an object of type list
stuff.append('python')           #call the append method
stuff.append('chuck')            #call the append method
stuff.sort()                     #calls the sort() method
print (stuff[0])                 #retrieves the item at position 0
print (stuff.__getitem__(0))     #calls the __getitem__() method in the stuff list with a parameter of zero.
print (list.__getitem__(stuff,0))#verbose way of retrieving the 0th item in the list


#___________________________#
#taking inpute as an list

# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 

#___________________________#
#Filter() function in python use two argument first is function and second one is list it will filter based on function


def is_even(n):
  return  n%2==0

def is_odd(n):
    return n%2!=0

nums = [233,5,32,2,21,34,56,6,7,8]

evens = list(filter(is_even,nums))              #list in return list()

odds = list(filter(is_odd,nums))              #list in return list()

print("Totals Enens:",evens)
print("-------------------------")
print("Totals Odds",odds)


#___________________________#
#map() in python
#takes value and apply some operation

nums = [233,5,32,2,21,34,56,6,7,8]

evens = list(filter(lambda n: n%2==0,nums))          #use lambda 

doubles = list(map(lambda n: n*2,evens))         #map also takes two argument function and the sequence

print(evens)
print(doubles)

#___________________________#
#reduce() in python


from functools import reduce

nums = [233,5,32,2,21,34,56,6,7,8]

evens = list(filter(lambda n: n%2==0,nums))              #use lambda 

doubles = list(map(lambda n: n*2,evens))         #map also takes two argument function and the sequence

print(doubles)

sum = reduce(lambda a,b:a+b,doubles)                 #reduce also takes two argument function and the sequence 

print(sum)

#________________________________________________________________________________________________________________________#
# convert one sequence to another

>>> set([1,2,3])
{1, 2, 3}
>>> tuple({5,6,7})
(5, 6, 7)
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
>>> dict([[1,2],[3,4]])             #To convert to dictionary, each element must be a pair
{1: 2, 3: 4}
>>> dict([(3,26),(4,44)])
{3: 26, 4: 44}


#________________________________________________________________________________________________________________________#

#_________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Tuple !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Tuples are very similar to list except that the whole set of elements are enclosed in parentheses instead of square brackets.
'''
You cannot add elements to a tuple.
You cannot append or extend a method.
You cannot remove elements from a tuple.
Tuples have no remove or pop method.
Count and index are the methods available in a tuple.
'''

>>> tupl
('Tuple', 'is', 'an', 'IMMUTABLE', 'list')
>>> tupl.append('new')
Traceback (most recent call last):
   File "<pyshell#148>", line 1, in <module>
      tupl.append('new')
AttributeError: 'tuple' object has no attribute 'append'
>>> tupl.remove('is')
Traceback (most recent call last):
   File "<pyshell#149>", line 1, in <module>
      tupl.remove('is')
AttributeError: 'tuple' object has no attribute 'remove'
>>> tupl.index('list')
4
>>> tupl.index('new')
Traceback (most recent call last):
   File "<pyshell#151>", line 1, in <module>
      tupl.index('new')
ValueError: tuple.index(x): x not in tuple
>>> "is" in tupl
True
>>> tupl.count('is')
1

#_________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  Dictionaries !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Dictionary is one of the Python’s built-in data types and it defines one-to-one relationships between keys and values.
'''
You cannot have duplicate keys in a dictionary. Altering the value of an existing key will delete the old value.
You can add new key-value pairs at any time.
Dictionaries have no concept of order among elements. They are simple unordered collections.
'''


>>> # empty dictionary
>>> my_dict = {}
>>>
>>> # dictionary with integer keys
>>> my_dict = { 1:'msft', 2: 'IT'}
>>>
>>> # dictionary with mixed keys
>>> my_dict = {'name': 'Aarav', 1: [ 2, 4, 10]}
>>>
>>> # using built-in function dict()
>>> my_dict = dict({1:'msft', 2:'IT'})
>>>
>>> # From sequence having each item as a pair
>>> my_dict = dict([(1,'msft'), (2,'IT')])
>>>
>>> # Accessing elements of a dictionary
>>> my_dict[1]
'msft'
>>> my_dict[2]
'IT'
>>> my_dict['IT']
Traceback (most recent call last):
   File "<pyshell#177>", line 1, in <module>
   my_dict['IT']
KeyError: 'IT'
>>>

#Modifying Dictionaries
>>> # Modifying a Dictionary
>>>
>>> my_dict
{1: 'msft', 2: 'IT'}
>>> my_dict[2] = 'Software'
>>> my_dict
{1: 'msft', 2: 'Software'}
>>>
>>> my_dict[3] = 'Microsoft Technologies'
>>> my_dict
{1: 'msft', 2: 'Software', 3: 'Microsoft Technologies'}

#Deleting Items from Dictionaries

>>> my_dict
{1: 'msft', 2: 'Software', 3: 'Microsoft Technologies', 4: 'Operating System',
'Bill Gates': 'Owner'}
>>>
>>> del my_dict['Bill Gates']
>>> my_dict
{1: 'msft', 2: 'Software', 3: 'Microsoft Technologies', 4: 'Operating System'}
>>>
>>> my_dict.clear()
>>> my_dict
{}


#_________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Set !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Python also includes a data type for sets. A set is an unordered collection with no duplicate elements.
#You can change elements of set unlike tuple.
#Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                                                        # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}

# fast membership testing
>>> 'orange' in basket                 
True
>>> 'crabgrass' in basket
False

# Demonstrate set operations on unique letters from two words

>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>>b
{'z', 'c', 'm', 'a', 'l'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}

#When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe

#Inline if elese(Ternary operator)/Conditional Operator
[on_True] if [expression] else [on_False]
>>>print('a is 20' if a==20 else 'a is not 20')             #Do somthing if condition else do somthing
>>>print('a is 20' if a==21 else 'a is not 20')	
>>>b = True if a==20 else False
>>>print(b)
True

#_________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! CSV !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#CSV Writing to a excel Book

#import Necessary
>>>from xlsxwriter import workbook

#make a workbook
>>>workbook = xlsxwriter.Workbook('filename.xlsx')

#Add a sheet
>>>worsheet = workbook.add_worksheet()

#write function Parameter - (row, colom, value)
>>>worsheet.write(0,0,'zero row and zero colom')
>>>worsheet.write(0,1,'zero row and First colom')
>>>worsheet.write(1,0,'First row and zero colom')
>>>worsheet.write(0,0,'First row and First colom')


#close workbook
>>>workbook.close()

#CSV Reading from a  excel Book











!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Reglar Expression !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Reglar Expression is a special sequence of charactor that helps you match or find other strings or set of strings using a specialized syntex held in pattern.
# ^ --> Matches begining of Line
# $ --> Matches end of line
#. --> Maches any single charactor except newline(using m allow it to match newline as well)
#[...] --> Matches any single charactor in brackets.
#[^...] --> Matches any single charactor not in brackets.
#re* --> Matches 0 or more occurences of preceding expression.
#re+ --> Matches 1 or more occurence of preceding expression.
#re? --> Matches o or 1 occurence of preceding expression.
#re{n} --> Matches exactly n number of occurence of preceding expression.
#re{n,} --> Matches n or more occurence of preceding expression.
#re{n,m} -->Matches atleast n and at most m occurence of preceding expression.
#a|b --> Matches either a or b.
#(re) --> Group regular expression and remember matches text


#Functions of Regular expression:
--Match  --> try to apply the pattern at the start of the string, returning a match object, or none if no match was found.
--Search --> Scan through string looking for a match to the pattern, returning a match object, or none if no match was found.
--Sub --> substitute
--subn --> 
--findall --> match all occurence of a pattern, not just the first one as searh() does.
--finditer
--purge
--split  --> split the sourse string by the occurence of the pattern, returning a list containing the resulting substring.

>>>import re                             #regular string module
>>>m = re.match("^123","123456789")      # check 123 is present at starting of the string or not (pattern, string, flag)(match check only begning of the string)
>>>print(m.group(0))                     # check for group 0
123

#Check charactors in ending of the string
>>>m= re.search("890$","1234567890")       #serach function search in all bengning,middle,end but match only check at begning.
>>>print(m.group(0))  

#findall function(Split string on base of pattern)
>>> m = re.findall("890","12345678901234567890123456789012345678901234567890123456789012345678901234567890")
>>>print(m)                                                                                                   #return match string in a list
['890', '890', '890', '890', '890', '890', '890', '890']    

#sun function
>>>m = re.sub("12","34","121212121212121212",2)            #replace(substitute) 12 by 34(old,new, string)[last n = 2 means only two time substitue]
>>>print(m)
343434343434343434

#split function
>>>m = re.split(",","1,2,3,4,5,6,7,8,9")              #split on the basis of pattern here on base of comma
>>>print(m)                       
['1', '2', '3', '4', '5', '6', '7', '8', '9']

>>> name = 'John Smith'
>>> first_name, last_name = name.split()
>>> print(last_name, first_name, sep=', ')
'Smith, John'

#________________________________________________#
#Validate Email syntex using regular expression

# \w   --> it is used for all a-z,A-z,0-9 All Alphanumeric Values and underscore
# (Dot.) --> In the default mode, this mathes any character expect new line 
>>>import re
>>>m= re.search(r"[\w]+@[\w]+[.][\w]+","test@gmail.comm")
>>>print(m.group(0))
test@dmail.com                                                   #print email only if syntext is right otherwise return none

#________________________________________________#
#Program for ip filtering and replace it with new one
import re
reg_exp = "([\d]{1,3}\.){3}[\d]{1,3}"   #[\d] it is for digit {1,3} --> it means three times only and {3} --> means it will come three times                                  
sub_str = re.sub(reg_exp,"0.0.0.0","Here Ip IS 12.34.56.22")       #replace reg_exp with 0.0.0.0 in string 
print(sub_str)

#________________________________________________#
#mac address substitution in string
import re
mac_add = "AB:CD:EF:12:A1:B3"                 #IN COMBINATION OF TWO DIGIT IN SIX SECTION
expr = "([A-Z0-9]{2}[:]){5}[0-9A-Z]{2}"              #
sub_str=re.sub(expr,"12:23:45:56:87:00",mac_add)
print(sub_str)

#________________________________________________#
#Extract E-mail from text
>>>import re                                                                               #import regular expression package
>>>text = "Please contact us at contact@tutorialspoint.com for further information."+\
        " You can also give feedbacl at feedback@tp.com"                                   #text containing Email   


emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)                      #Extract Email
print(emails)                                                                              #print 

#________________________________________________#
#Extract URL's From text
>>>import re
 
>>>with open("path\url_example.txt") as file:
        for line in file:
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            >>>print(urls)

#_______________________________________________________________________________________________#

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  File  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""

#Creating the text File

file = open("testfile.txt","w")                     #creating a file 
 
#writing text to file
file.write("Hello World")                          #writing in to it 
file.write("This is our new text file")            #writing in to it
file.write("and this is another line.")            #writing in to it
file.write("Why? Because we can.")                 #writing in to it
file.close()                                       #closing file

#Reading a file
with open("testfile.txt") as f:                 #use the with keyword when dealing with file objects
print(f.read())


>>>print(file.read(10))                   #read only first 10 charactors

>>>print(file.readline())                        #read line by line

>>>fh = open("hello.txt", "a")              #for append 
>>>fh.write("We Meet Again World") 
>>>fh.close 

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#______________________________________________________________________________________________________________________________#
# Python code to illustrate generator expression  
generator = (num ** 2 for num in range(10))  
for num in generator: 
    print(num) 

#We can also generate a list using generator expressions :
string = 'geek'
li = list(string[i] for i in range(len(string)-1, -1, -1)) 
print(li) 















































































































































