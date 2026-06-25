print("hello world")
a=8
print(type(a))
# arithmetic operator
print(a+8)
print(a*8)
print(a-8)
print(a/8)
print(a%8)

print(a//8)
print(a**2)

print(2*2+(2-2))

# increment and decremnet operator

a=a+1
print(a)

a+=1
print(a)
a/=2
print(a)


a=-1
abs(a)
a=-1.99
a=abs(a)
round(a)

# string
st="123"
print(type(st))

from sys import getsizeof
st="hello moto"
print(st)
st="hello'oto"
print(getsizeof(st))

st="hello\'oto"
print(getsizeof(st))
print(st)

print(st[3])
print(st[1:2])
print(st[::2])
print(st[::-1])
print(st[-1::-1])
print(st[-1:-10:-1])

st="no guts"
print(st.lower())
print(st.upper())

print(st.count('n'))
print(st.find('ni'))#return the index of the string #return -1 if not found

print(len(st))
print(st.replace("n","y"))

name="nirmal"
srr="nk"
print(name+' as '+srr)

# format
srr="nirmal"
srr2="thestr"
srr3="{0} {1}".format(srr,srr2)
srr4=f'{srr2} result'
print(srr4)

print(dir(srr))
print(help(str))

#type conversion

x="9"
print(type(x))
l=int(x)
print(l)
print(type(l))

# list[]

list1=['nirmal',1,2,3,'hi']
alpha=[]
numb=[]
for i in range(len(list1)):
    if type(list1[i])==str:
        alpha.append(list1[i])
    else:
        numb.append(list1[i])

print(list1)
print(alpha)
print(numb)

l=" ".join(["nk","pk"])
l.split()
stu="nimal was sleeping"
stu.strip("n g i")
list1=list(range(10))
list2=list(reversed(range(10)))
list(zip(list1,list2))
dict(zip(list1,list2))

dict1=["nirmal","ravi","ragu","raj"]
dict2={90,50,60,20}
l=zip(dict1,dict2)
for i,j in zip(dict1,dict2):
    print(i,j)

list1=["yellow","ravi"]
list2=["nirmal","ravi"]

for i in range(len(list1)):
    if list1[i] in list2:
        print(f'{list1[i]} is a name')
    else:
        print(f'{list1[i]} is a color')