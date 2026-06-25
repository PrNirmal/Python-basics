# int,float,complex

# operators
# arthmetic operator
# +,-,/,*,%,//,**

# add
a=7
b=3
a+b
a-b
a*b
a**b #exponent 6^3
a//b #makes it floor of the value
# 15/2
# 15//2

a%b

# assignment operator

# List,tuple,dict,set
a=4
# List

# Indexed,ordered,allows duplicate,mutable


list_1=["nirmal",24,32] #1D List
list_1[0]
list_1[1]
list_1[2]
# list_1[3]
list_2=["nirmal",24,[21,"Vishal"]] #2D List
# 0-length of list-1
list_2[0]
list_2[1]
list_2[2][1]

dir([])

# methods in list
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# append
list_3=["Nirmal","ajay"]
list_3.append("gokul")
list_3
list_3[0]="vishal"

# sort
list_3=[1,25,3]
list_3=["Nirmal","ajay"]
list_3.sort(reverse=True)

# tuple
# ordered,indexed,allows duplicate,immutable

tuple_1=("Nirmal",23)
tuple_1[1]


# set
# unordered,not indexed,don't allow duplicate

# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset', # 'issuperset', 'pop', 'remove',
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

set_1={}
set_2={"nirmal","ajay","gokul"}

dir(set)

# dict
#  allow duplicate,Key-values,key=>value
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

dict_1={"names":["nirmal","ajay","gokul"],3:["nirmal"],1:3}
dict_1["names"]
dict_1[1]

# conditions
# if,elif,else
a=11
if a==10:
    print("Its 10")
else:
    print("Its Not 10")
a=221
if a==10:
    print("Its 10")
elif a<=10:
    print("Its less than 10")
elif a>=10 and a<=20:
    print("Its Greater than 10 and less than 20")
else:
    print("Its Greater than 20")