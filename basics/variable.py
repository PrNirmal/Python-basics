# variable syntax
var='kav'
_var='kav'
v_ar='kav'
v__='kav'
_V_='kav'
print(var)
print(_var)
print(v_ar)
print(v__)
print(_V_)
# invalid
# 2var='kav'
# v-ar='kav'
# v ar='kav'
# print(2var)
# print(v-ar)
# print(v ar)
#
my_var_name='kav'#easy to read the variable name
MyVarName='kav'
myVarName='kav'
# creating variable
x=2#variables automatically created when we are assigning values to it.
y='abc'
print(x)
print(y)
# to find type of it
x=2
y='abc'
print(type(x))
print(type(y))
#  variables are case sensitive
x='a'#small x
X='c'#capital X
# small and capital letters are different,will not overwrite
# x='b'#it will overwrite the values,giving the same variable name
print(x)
print(X)
#
x=4
x=3#it will overwrite the values,giving the same variable name
print(x)
print(x)
# multiple values to multiple variables in one line
# x,y,z='one','two','three','o'#no of variables=no of values,otherwise will be error(unpack)
x,y,z='one','two','three'
print(x,y,z)
print(x)
print(y)
print(z)
# one value to multiple variables
x=y=z='ant'
print(x)
print(y)
print(z)
# packing =assigning values to a tuple 'and' unpacking=extract values back to a variable
fruits=('apple','banana','cherry')
(rice,food,bat)=fruits
# print(fruits)
print(rice,food,bat)

