#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to get the Python version you are using.
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[2]:


#Write a Python program to display the current date and time.
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[4]:


# Write a Python program which accepts the radius of a circle from the user and compute the area
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[5]:


#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


# In[ ]:


#Write a Python program to accept a filename from the user and print the extension of that.
#filename = input("Input the Filename: ")
#f_extns = filename.split(".")
#print ("The extension of the file is : " + repr(f_extns[-1]))


# In[6]:


#Write a Python program to display the first and last colors from the following
list = ["Red","Green","White" ,"Black"]
print(list[0],list[-1])


# In[9]:


#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n=int(input("enter the number"))
print(n+n*n+n*n*n)


# In[10]:


#Write a Python program to print the calendar of a given month and year.
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))


# In[11]:


# Write a Python program to calculate number of days between two dates.
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)


# In[12]:


# Write a Python program to get the volume of a sphere with radius 6.
pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)


# In[13]:


#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(difference(22))
print(difference(14))


# In[14]:


#Write a Python program to test whether a number is within 100 of 1000 or 2000.
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))


# In[15]:


#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
def sum_thrice(x, y, z):

     sum = x + y + z
  
     if x == y == z:
      sum = sum * 3
     return sum

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))


# In[16]:


#Write a Python program to count the number 4 in a given list.
list=[1,4,4,5,4]
list.count(4)


# In[18]:


#Write a Python program to test whether a passed letter is a vowel or not.
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))    


# In[19]:


#Write a Python program to create a histogram from a given list of integers.
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])


# In[20]:


#Write a Python program to concatenate all elements in a list into a string and return it.
def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([1, 5, 12, 2]))


# In[21]:


#Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)
		


# In[22]:


#Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))


# In[23]:


#Write a Python program that will accept the base and height of a triangle and compute the area.
b = int(input("Input the base : "))
h = int(input("Input the height : "))

area = b*h/2

print("area = ", area)


# In[24]:


#Write a Python program to compute the greatest common divisor (GCD) of two positive integers
def gcd(x, y):
    gcd = 1
    
    if x % y == 0:
        return y
    
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd

print(gcd(12, 17))
print(gcd(4, 6))


# In[25]:


#Write a Python program to get the least common multiple (LCM) of two positive integers.
def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm
print(lcm(4, 6))
print(lcm(15, 17))


# In[26]:


#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum

print(sum(2, 1, 2))
print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3))


# In[27]:


#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))


# In[28]:


#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
def test_number5(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False

print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))


# In[29]:


# Write a Python program to add two objects if both objects are an integer type
def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
         raise TypeError("Inputs must be integers")
    return a + b

print(add_numbers(10, 20))


# In[30]:


#Write a Python program to solve (x + y) * (x + y).
x=4
y=3
print((x+y)*(x+y))


# In[31]:


#Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)


# In[33]:


#Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import struct
print(struct.calcsize("P") * 8)


# In[34]:


#Write a Python program to get OS name, platform and release information
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())


# In[35]:


#Write a Python program to parse a string to Float or Integer.

n = "246.2458"
print(float(n))
print(int(float(n)))


# In[37]:


#Write a Python program to list all files in a directory in Python.

#from os import listdir
#from os.path import isfile, join
#files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
#print(files_list);


# In[38]:


#Write a Python program to print without newline or space.

for i in range(0, 10):
    print('*', end="")
print("\n")
	


# In[39]:


#Write a Python program to determine profiling of Python programs.
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')


# In[40]:


#Write a Python program to print to stderr. 
from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")


# In[41]:


#Write a python program to access environment variables.
import os
# Access all environment variables 
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable 
#print(os.environ['HOME'])
#print('*----------------------------------*')
#print(os.environ['PATH'])
#print('*----------------------------------*')


# In[42]:


#Write a Python program to get the current username
import getpass
print(getpass.getuser())


# In[43]:


#Write a Python to find local IP addresses using Python's stdlib
import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


# In[45]:


#Write a Python program to get height and width of the console window.
"""def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

print('Number of columns and Rows: ',terminal_size())"""


# In[46]:


#Write a program to get execution time for a Python method.
import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))


# In[47]:


#Write a python program to find the sum of the first n positive integers.

n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print(sum_num)


# In[48]:


#Write a Python program to convert height (in feet and inches) to centimeters.

print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)


# In[49]:


#Write a Python program to calculate the hypotenuse of a right angled triangle.
from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))

c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is", c )


# In[50]:


#Write a Python program to convert the distance (in feet) to inches, yards, and miles.
d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)


# In[1]:


# Write a Python program to convert all units of time into seconds.
days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = days + hours + minutes + seconds

print("The  amounts of seconds", time)


# In[2]:


# Write a Python program to get an absolute file path.
def absolute_file_path(path_fname):
        import os
        return os.path.abspath('path_fname')        
print("Absolute file path: ",absolute_file_path("test.txt"))


# In[4]:


#Write a Python program to get file creation and modification date/times.
#import os.path, time
#print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
#print("Created: %s" % time.ctime(os.path.getctime("test.txt")))


# In[5]:


#Write a Python program to convert seconds to day, hour, minutes and seconds.
time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


# In[6]:


#Write a Python program to calculate body mass index.
height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))


# In[7]:


# Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
kpa = float(input("Input pressure in in kilopascals> "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))


# In[8]:


#Write a Python program to calculate the sum of the digits in an integer.
num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)


# In[9]:


#Write a Python program to sort three integers without using conditional statements and loops.
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)


# In[10]:


#Write a Python program to sort files by date.
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))
	


# In[11]:


#Write a Python program to get a directory listing, sorted by creation date.
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))
	


# In[12]:


#Write a Python program to get the details of math module.
import math            
math_ls = dir(math)
print(math_ls)


# In[13]:


#Write a Python program to hash a word.
soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
 
word=input("Input the word be hashed: ")
 
word=word.upper()
 
coded=word[0]
 
for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])
print() 
print("The coded word is: "+coded)
print()


# In[14]:


#Write a Python program to get the copyright information. 76.
import sys
print("\nPython Copyright Information")
print(sys.copyright)
print()


# In[15]:


#Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.

import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))


# In[16]:


#Write a Python program to test whether the system is a big-endian platform or little-endian platform.

import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()


# In[17]:


#Write a Python program to find the available built-in modules.

import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))


# In[18]:


#Write a Python program to get the size of an object in bytes.
import sys
str1 = "one"
str2 = "four"
str3 = "three"
print()
print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")
print()


# In[19]:


#Write a Python program to get the current value of the recursion limit.

import sys
print()
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())
print()


# In[20]:


#Write a Python program to concatenate N strings.
list_of_colors = ['Red', 'White', 'Black']  
colors = '-'.join(list_of_colors)
print()
print("All Colors: "+colors)
print()


# In[21]:


#Write a Python program to calculate the sum over a container.

s = sum([10,20,30])
print("\nSum of the container: ", s)
print()


# In[22]:


#Write a Python program to test whether all numbers of a list is greater than a certain number.

num = [2,3,4]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print()


# In[23]:


#Write a Python program to count the number occurrence of a specific character in a string.

s = "The quick brown fox jumps over the lazy dog."
print()
print(s.count("q"))
print()


# In[25]:


#Write a Python program to check whether a file path is a file or a directory.
"""import os

#checks if path is a file
isFile = os.path.isfile(fpath)

#checks if path is a directory
isDirectory = os.path.isdir(fpath)"""


# In[26]:


#Write a Python program to get the ASCII value of a character

c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))


# In[28]:


#Write a Python program to get the size of a file.
#import os
#file_size = os.path.getsize("abc.txt")
#print("\nThe size of abc.txt is :",file_size,"Bytes")
#print()


# In[29]:


#Write a Python program to perform an action if a condition is true. Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.

n=1
if n == 1:
    print("\nFirst day of a month")
print()


# In[30]:


#Given variables x=30 and y=20, write a Python program to print t "30+20=50".

x = 30
y = 20
print("\n%d+%d=%d" % (x, y, x+y))
print()


# In[31]:


#Write a Python program to create a copy of its own source code.

print()
print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))())
print()


# In[32]:


#. Write a Python program to swap two variables.
a=4
b=5
a,b=b,a
print(a,b)


# In[33]:


#Write a Python program to define a string containing special characters in various forms.
print()
print("\#{'}${\"}@/")
print("\#{'}${"'"'"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')
print()


# In[35]:


# Write a Python program to get the identity of an object.

obj1 = object()
obj1_address = id(obj1)
print()
print(obj1_address)
print()


# In[37]:


#Write a Python program to convert a byte string to a list of integer
x = b'Abc'
print()
print(list(x))
print()


# In[38]:


#Write a Python program to check whether a string is numeric
str = 'a123'
#str = '123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()


# In[39]:


# Write a Python program to print the current call stack.

import traceback
print()
def f1():return abc()
def abc():traceback.print_stack()
f1()
print()


# In[40]:


#Write a Python program to list the special variables used within the language.

s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print()
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )
print()


# In[41]:


#Write a Python program to get the system time. Note: The system time is important for debugging, network information, random number seeds, or something as simple as program performance.

import time
print()
print(time.ctime())
print()


# In[42]:


# Write a Python program to clear the screen or terminal.

import os
import time
# for windows
# os.system('cls')
os.system("ls")
time.sleep(2)
# Ubuntu version 10.10
os.system('clear')


# In[43]:


#Write a Python program to get the name of the host on which the routine is running.

import socket
host_name = socket.gethostname()
print()
print("Host name:", host_name)
print()


# In[44]:


# Write a Python program to access and print a URL's content to the console.

from http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)


# In[45]:


#Write a Python program to get system command output.

import subprocess
# file and directory listing
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)


# In[46]:


# Write a Python program to extract the filename from a given path.

import os
print()
print(os.path.basename('/users/system1/student1/homework-1.py'))
print()


# In[48]:


#Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process. Note: Availability: Unix.
"""import os
print("\nEffective group id: ",os.getegid())
print("Effective user id: ",os.geteuid())
print("Real group id: ",os.getgid())
print("List of supplemental group ids: ",os.getgroups())
print()
"""


# In[49]:


# Write a Python program to get the users environment.

import os
print()
print(os.environ)
print()


# In[50]:


#Write a Python program to divide a path on the extension separator.

import os.path
for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
    print('"%s" :' % path, os.path.splitext(path))
	


# In[52]:


#Write a Python program to retrieve file properties
"""import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))
"""


# In[54]:


#Write a Python program to find path refers to a file or directory when you encounter a path name
"""import os.path

for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))
	"""


# In[55]:


# Write a Python program to check if a number is positive, negative or zero
num = float(input("Input a number: "))
if num > 0:
   print("It is positive number")
elif num == 0:
   print("It is Zero")
else:
   print("It is a negative number")
   


# In[56]:


#Write a Python program to get numbers divisible by fifteen from a list using an anonymous function

num_list = [45, 55, 60, 37, 100, 105, 220]
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)


# In[57]:


#Write a Python program to make file lists from current directory using a wildcard.

import glob
file_list = glob.glob('*.*')
print(file_list)


# In[58]:


#Write a Python program to remove the first item from a specified list

color = ["Red", "Black", "Green", "White", "Orange"]
print("\nOriginal Color: ",color)
del color[0]
print("After removing the first color: ",color)
print()


# In[59]:


#Write a Python program to input a number, if it is not a number generate an error message.
while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()
	


# In[60]:


# Write a Python program to filter the positive numbers from a list
nums = [34, 1, 0, -23]
print("Original numbers in the list: ",nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Positive numbers in the list: ",new_nums)


# In[61]:


#Write a Python program to compute the product of a list of integers (without using for loop).

from functools import reduce
nums = [10, 20, 30,]
nums_product = reduce( (lambda x, y: x * y), nums)
print("Product of the numbers : ",nums_product)


# In[62]:


#Write a Python program to prove that two string variables of same value point same memory location
str1 = "Python"
str2 = "Python"
 
print("\nMemory location of str1 =", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))
print()


# In[63]:


# Write a Python program to create a bytearray from a list

print()
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)
print()


# In[64]:


# Write a Python program to display a floating number in specified numbers


order_amt = 212.374
print('\nThe total order amount comes to %f' % order_amt)
print('The total order amount comes to %.2f' % order_amt)
print()


# In[65]:


#Write a Python program to format a specified string to limit the number of characters to 6.

str_num = "1234567890"
print()
print('%.6s' % str_num)
print()


# In[1]:


# Write a Python program to determine whether variable is defined or not
try:
  y
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
 


# In[2]:


#Write a Python program to empty a variable without destroying it Sample data: n=20 d = {"x":200} Expected Output : 0 {}.
n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)()) 


# In[3]:


#Write a Python program to determine the largest and smallest integers, longs, floats.
import sys
print("Float value information: ",sys.float_info)
print("\nInteger value information: ",sys.int_info)
print("\nMaximum size of an integer: ",sys.maxsize) 


# In[4]:


#Write a Python program to check whether multiple variables have the same value.
a=b=c=20
if a==b==c==20:
    print("allvariables have same values")


# In[5]:


#. Write a Python program to sum of all counts in a collections?

import collections
num = [2,2,4,6,6,8,6,10,4]
print(sum(collections.Counter(num).values()))


# In[6]:


# Write a Python program to get the actual module object for a given object

from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))


# In[7]:


#Write a Python program to check whether an integer fits in 64 bits.

int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())
	


# In[8]:


# Write a Python program to check whether lowercase letters exist in a string


str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))


# In[9]:


# Write a Python program to add leading zeroes to a string

str1='122.22'
print("Original String: ",str1)
print("\nAdded trailing zeros:")
str1 = str1.ljust(8, '0')
print(str1)
str1 = str1.ljust(10, '0')
print(str1)
print("\nAdded leading zeros:")
str1='122.22'
str1 = str1.rjust(8, '0')
print(str1)
str1 = str1.rjust(10, '0')
print(str1)


# In[10]:


# Write a Python program to use double quotes to display strings

import json
print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))


# In[11]:


# Write a Python program to split a variable length string into variables


var_list = ['a', 'b', 'c']
x, y, z = (var_list + [None] * 3)[:3]
print(x, y, z)
var_list = [100, 20.25]
x, y = (var_list + [None] * 2)[:2]
print(x, y)


# In[12]:


# Write a Python program to list home directory without absolute path

import os.path
print(os.path.expanduser('~'))


# In[14]:


# Write a Python program to input two integers in a single line

print("Input the value of x & y")
x, y = map(int, input().split())
print("The value of x & y are: ",x,y)


# In[15]:


# Write a Python program to print a variable without spaces between values Sample value: x =30

x = 30
print('Value of x is "{}"'.format(x))


# In[17]:


#Write a Python program to find files and skip directories of a given directory
"""import os
print([f for f in os.listdir() if os.path.isfile(os.path.join('/home/students', f))])
"""


# In[18]:


#. Write a Python program to convert true to 1 and false to 0

x = 'true'
x = int(x == 'true')
print(x)
x = 'abcd'
x = int(x == 'true')
print(x)


# In[19]:


#. Write a Python program to valid a IP address.

import socket
addr = '127.0.0.2561'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")
	


# In[20]:


#Write a Python program to convert an integer to binary keep leading zeros Sample data: 50

x = 12
print(format(x, '08b'))
print(format(x, '010b'))


# In[21]:


#Write a python program to convert decimal to hexadecimal Sample decimal number: 30, 4

x = 30
print(format(x, '02x'))
x = 4
print(format(x, '02x'))


# In[22]:


#Write a Python program to find the operating system name, platform and platform release date.

import os, platform
print("Operating system name:")
print(os.name)
print("Platform name:")
print(platform.system())
print("Platform release:")
print(platform.release())


# In[23]:


# Write a Python program to check whether variable is of integer or string


print(isinstance(25,int) or isinstance(25,str))
print(isinstance([25],int) or isinstance([25],str))
print(isinstance("25",int) or isinstance("25",str))


# In[24]:


# Write a Python program to test if a variable is a list or tuple or a set

x = ['a', 'b', 'c', 'd']
x = {'a', 'b', 'c', 'd'}
x = ('tuple', False, 3.2, 1)
if type(x) is list:
    print('x is a list')
elif type(x) is set:
    print('x is a set')
elif type(x) is tuple:
    print('x is a tuple')    
else:
    print('Neither a list or a set or a tuple.')


# In[25]:


#Write a Python function to check whether a number is divisible by another number. Accept two integer’s values form the user

def multiple(m, n):
	return True if m % n == 0 else False

print(multiple(20, 5))
print(multiple(7, 2))


# In[26]:


#Write a Python function to find the maximum and minimum numbers from a sequence of numbers.

def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))


# In[27]:


#Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number

def sum_of_cubes(n):
  n -= 1
  total = 0
  while n > 0:
    total += n * n * n
    n -= 1
  return total
print("Sum of cubes: ",sum_of_cubes(3))


# In[28]:


#Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values.

def odd_product(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        if product & 1:
          return True
          return False
          
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
print(dt1, odd_product(dt1));
print(dt2, odd_product(dt2));


# In[ ]:




