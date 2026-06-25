# Lists are used to store multiple items in a single variable
# List items are ordered, changeable, and allow duplicate values

# append
list_v=[2,4,7]#it will add at the end
list_v.append(3)
print(list_v)

# clear
list_s8=['an','k','are','was']#used to clear the list
list_s8.clear()
print(list_s8)

# copy
list_11=['an','are','was']
list_12=list_11.copy()#used to copy the list
print(list_12)

# count
list_s4=[1,2,2,2,5,5,7,'s']#used to count no of times the item is present
list_s4.count(2)
list_s4.count('s')
list_s4.count(0)#if the element found return 0

# extend
list_s9=[4,5,6]#used to merge two list
list_s10=['so','hi']
s=list_s9+list_s10
print(s)
list_s9.extend(list_s10)
print(list_s9)

# index
list_13=['an','are','was']
list_13.index('are')#used to find the index of the item

# insert
list_s2=[1,2,5,7,9]#it will insert the item at the position(index)
list_s2.insert(2,'a')
print(list_s2)

# pop
list_s7=['an','are','was']#it will pop the last value in the list
list_s7.pop()#the element will be removed
print(list_s7)
list_s7.pop(1)#you can also mention the index to pop
print(list_s7)

# remove
list_s3=[1,8,5,7,'s']
list_s3.remove(5)#it will remove the value mentioned
list_s3.remove('s')
print(list_s3)

# reverse
list_s6=[9,1,5,2,4,2]#it will reverse the list
list_s6.reverse()
print(list_s6)

# sort
list_s5=[9,1,5,2,4,2]#it will sort the list
list_s5.sort()#ascending
print(list_s5)
list_s5.sort(reverse=True)#decending using 'reverse=true' keyword
print(list_s5)


# add two list and sort it
list_a=[1,3,5,7]
list_b=[0,2,4,6]
list_a.extend(list_b)
print(list_a)
list_a.sort()
print(list_a)
#for,range
list_a3=[2,4,6]  # if c<a:#c>a:
list_a3=['ab','cdeccc','mkm','fghi','jkl']
# list_a3=['ab','jkl','fghi','cdeccc']
# list_a3=['aaa','cdeccc','jkl','fghi','ab']
list_a3=['ab','cdeccc','mkm','fghi','jkl']
list_a3=['ab','ccc','ddd','s']
k=''
c=3
# c=len(list_a3[0])
for i in list_a3:
    print(len(i))
    a=len(i)
    # if c<a:
    #     # k = i
    #     c=a
    if c==a:
        k = i
        c=a
print(k)

    # print(len(list_a3))
#

list( range(10))
list(range(5,10))

#
for i in range(10):
    if i<5:
        print(i)
#
for i in list_a3:
    print(i)
#step
list(range(2,50,10))
for i in range(2,50,10):
    print(i)
#len:length of string
list_a3=[2,4,6]
print(len(list_a3))
#
# for i in (len(list_a3)):
    # print(i)
#
for i in range(len(list_a3)):
    # print(i)
    print(list_a3[i])
#
list_a3=[2,4,6]
i=0
# 0<3
while i <len(list_a3):
    print(list_a3[i])
    i=i+1
#
# for i in range(len(list_a6)):no need..length is already defined to range..that is 4
list_a5=[10,102,4,66]
list_a6=[1,30,5,1]
for i in range(len( list_a5)):
    # print(i)
    print(list_a5[i])
    print(list_a6[i])
#
list_a5=[10,102,4,66]
list_a6=[1,30,5,1]
list_a7=[]
for i in range(len(list_a5)):
    # print(i)
    list_a7.append(list_a5[i])
    list_a7.append(list_a6[i])
print(list_a7)
#
list_=[[1,2,3],[8,4],[56,6]]
temp=[]
for i in list_:
    # print(i)
    for j in i:
        # print(j)
        temp.append(j)
print(temp)
#max repeated value
a=[1,2,1,4,4,1,2,5,2,1,1]
# set(a)
# max(a) dout
m=max(set(a),key=a.count)
print(m)
# check if item exists,using 'in' keyword
thislist=['a','b','c']
# print('a' in thislist)
if 'a' in thislist:
    print('ok')
#hw
thislist=['a','b','c','d','e']
thislist[1]='d'
thislist[1:3]=['v','m']
print(thislist)
# delete list
list_=[2,3,4]
del list_
print(list_)
#HOME WORK
list_1=['a','b']
list_2=['c','d','e']
list_2.extend(list_1)
print(list_2)
list_2.remove('e')
#
list_3=['r','s','t','i']
list_3.append('k')
print(list_3)
list_3.pop()
del list_3
#
list_4=[2,3,4,5]
print(list_4)
dict_2={'fruit1':'apple','fruit2':'mango'}
print(dict_2)
#check a string is anagram
str1='silent'
str2='listen'
if sorted(str1)==sorted(str2):
    print('anagram')
else:
    print('not anagram')

#silent to listen
x='silent'
print(x[2]+x[1]+x[0]+x[5]+x[3]+x[4])
#check a string is palindrome
str=input('enter string')
if str==str[::-1]:#reverse os string
    print('palindrome')
else:
    print('not palindrome')
#hw
animal={'rabbit':'carrot','deer':'grass','lizard':'insects'}
print(animal.keys())
#hw
num=3
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
    print(num,factorial)

name=input().split()