# a tuple is like a list, it uses () instead of[],also tuple defined using commas
# List items are ordered, changeable, and allow duplicate values

rgb=('red','blue','green')
print(rgb[0])
print(rgb[1])
print(rgb[2])
# tuple is immutable
rgb=('red','blue','green')
rgb[0]='white'#can't change
# definining a tuple that has 1 element
#creates empty tuple
numbers=(3,)
numbers_0=3,
numbers_1=1,2
numbers_2=(1,2)
print(type(numbers))
#
# numbers=(3,)
numbers=(3)
print(type(numbers))
# unpack a tuple
x,y,z=1,2,3
# x,y=1,2,3
x,y,_=1,2,3#we can use dummmy variable '_'
# x,*y,*z=(1,2,3,4,5,6,7,8)
x,y,*z=(1,2,3,4,5,6,7,8)#unpacking 1st two elements and packing leftover elements is a other variable.

# count
tup_1=(1,2,3,4)#used to count the no of times present
tup_1.count(1)
# index
tup_1=(1,2,3,4)#used find the index of the value
tup_1.index(3)
tup_1.index(1,0,2)#you can also set the start and end index


file=open("nirmal","rb")
file.read(3)
file.close()