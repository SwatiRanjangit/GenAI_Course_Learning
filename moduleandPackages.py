'''
modules and packages help organize and reuse code.
'''

'''
import math 

print(math.sqrt(16))

from math import sqrt,pi
from math import *(all functions inside this pakage)

print(sqrt(16))
print(pi)


import numpy as np

print(np.array([1,2,3,4]))


#CUSTOM PACKAGES

from packages.maths import addition

print(addition(3,3))



from packages.maths import *

print(addition(3,3))
print(subtraction(5,2))


from packages.subpackage.mult import multiplication

print(multiplication(3,3))




import array

arr = array.array('i',[1,2,3,4])
print(arr)



import random as r

print(r.randint(1,10))
print(r.choice(['apple','banana','lichi']))


# File and Directory access
import os as o
print(o.getcwd())
o.mkdir('test')



#High level of operations on files and collections of files
import shutil as s

s.copyfile('sample.txt','sample2.txt')

# Data serialization

import json as j

data = {'name':'krish','age':23}

json_str=j.dumps(data)
print(json_str)
print(type(json_str))

print(j.loads(json_str))
print(type(j.loads(json_str)))


#CSV

import csv

with open('example.csv',mode='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['krish',24])
    
with open('example.csv',mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



# datetime 

from datetime import datetime,timedelta

now= datetime.now()
print(now)

yesterday= now - timedelta(days=1)
print(yesterday)



import time

print(time.time())
time.sleep(2)
print(time.time())


#Regular expression

import re 

pattern=r'\d+'

text='There is 123 apples 456'

match=re.search(pattern,text)
print(match.group())



#create new directoty

import os

new_dir = "package"
os.mkdir(new_dir)
print(f"Directoty '{new_dir}' created")



#list files and directory

import os

items=os.listdir('.')
#print(items)


#JOINING PATH
#Relative path
dir_name="folder"
file_name="file.txt"
full_path=os.path.join(dir_name,file_name)
#print(full_path)

#full path
dir_name="folder"
file_name="file.txt"
full_path=os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)
'''
import os

path = 'example1.txt'
if os.path.exists(path):
    print(f"Path {path} exists")
else:
    print("path not exists")
    
path = 'example.txt'
if os.path.isfile(path):
    print(f"Path {path} is a file")
elif os.path.isdir(path):
    print("path is directoty")
else:
    print("None")
    
#Get absolute path

relative_path='example.txt'
absolute_path=os.path.abspath(relative_path)
print(absolute_path)






