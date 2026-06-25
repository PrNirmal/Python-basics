import os
import os as ram # os into ram
locals()
globals()
from os import remove
from os import remove as ram
from os import remove,listdir as l
from os import remove as r,listdir as l
from os import *

# functions
a,b=1,2
# first_variable=[]
a,b,c=(1,2,3)
print(a,b)
#functions
def sq():
    # print("hii")
    return 'hii'
print(sq())
#
def sq(a,b):
    # print(a+b)
    return a+b
print(sq(1,2))
# fn,parameter
k=4
def sq(a,b=0,c=1,d=k):
    # print(a,b,c)
    return a,b,c,d
# print(sq(1,3))#a=1
print(sq(a=0,c=2))
#
# def add(**values):#dout
def add(*values):
    # return values
    # print(values)
    for i in values:
        print(i)
# k=(1,2,3,4,5,5,6)
# print(add(k))
print(add(1,2,3,4,5,5,6))
#
list=[1,2,3,4,5,6]
# print(list)
add(*list)
#ifweneedtousedictionarytoafunctionweneedtouse **totheargument.
# def add(*kwargs):
def add(**kwargs):
    print(kwargs)
    # print(type(kwargs))
    print(kwargs['a'],kwargs['b'])
    # print(kwargs['a']+kwargs['b'])
    # h={'a':'b','c':'d'}
add(a=3,b=2)
add(a='h',b='d')#it prints into dictionary,because kwargs consider it as dict
#
def add(**kwargs):
    # print(kwargs['b'])
    print('it is'+' '+kwargs['b'])
add(a='h',b='d')
#
s={'a':1,'b':2}
def add(a,b):
    print(a,b)
# add(*s)
add(**s)
#
k=[1,2,3,4]
def add(*a):
    print(a)
    for i in a:
        print(i)
add(*k)
#
def my_function(*a):
# def my_function(a):
    # print(a+'hi')
    print(a)
# my_function('x')
# my_function('y')
# my_function('z')
# c='x','y','z'
# my_function(c)
my_function('x','y','z')
#
def my_function(a,b):
    print(a+b)
my_function('x','y')
# my_function('x')
#
def my_function(*a):
    print(a)
    # print('this is' +' '+a[2])
my_function('x','y','z')
#
def my_function(a,b,c):
    # print(a,b,c)
    print('this is'+' '+b)
my_function(a='x',b='y',c='z')
# default parameter
def add(a=0):
    print(a)
add(2)
add()
#
# def add(*food):
def add(food):
    for x in food:
        print(x)
fruits=['apple','banana','cherry']
add(fruits)
# add('apple','banana','cherry')

# return values
def add(x):
    return 5*x
print(add(3))