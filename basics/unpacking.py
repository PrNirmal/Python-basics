#unpack a list
colors=['red','blue','green']#pack
red,blue,green=colors#unpack
# red,blue=colors#can't unpack
colors,*x,y=['red','blue','green','white','yellow']
# colors=['red','blue','green','white','yellow']
# red,blue,*other=colors
tup,*reval=[1,2,3,4,5,6,7]
tup,*reval,x=[1,2,3,4,5,6,7]
tup,reval,*x,y=[1,2,3,4,5,6,7]
#
*a,=1,2
a,*b=1,2,3

# prime ok
n=int(input('enter n'))
for x in range(2,n):
    f=True
    for i in range(2,x):
        if x%i==0:
            f=False
    if f==True:
        print(x)

def prime(x):

     for i in range(2,x):
        if(x%i==0):
            print(x,"not a prime no")
            break
     else:
            print(x,"it is a prime no")

print(prime(3))

# fact
def fact(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p
n=int(input('enter n'))
f=fact(n)
print(f)

n=int(input('enter n:'))
x=int(input('enter x'))
s=0
for i in range(1,n+1):
    s=s+((x**i)/i)
print('sum of series',s)

n=int(input('enter n:'))
s=0


for i in range(1,n+1):
    s=s+i
print("sum=",s)



def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    return fact
n=int(input('enter n'))
print(factorial(n))

#
n=int(input('enter n'))
x=int(input('enter x'))
s=0
for i in range(1,n+1):
    s=s+((x**i)/i)
print(s)


# def count():
# n=sub_list.count(s)
# ['java', 'asp.net', 'lang', 'c#', 'c#', 'It']
sub_list=['java','asp.net','lang','c#','c#','It']
# def remove():
# def clear():
def count():
    s=input('enter n:')
    n = sub_list.count(s)
    # sub_list.remove(s)
    # sub_list.clear()
    print(s,n)
    print(sub_list)
count()
# clear()
# remove()



# count()

#
sub_list=['java','asp.net','lang','c#','it']
# def ascsort():
def descsort():
    # sub_list.sort()
    sub_list.sort(reverse=True)
    print(sub_list)
# ascsort()
descsort()
#
def length():
    str=input('enter n:')
    l=len(str)
    print(l)
length()
#
def cap():
    strg=input('enter n:')
    l=strg.capitalize()
    print(strg,l)
cap()
#
def swap():
    strg=input('enter n:')
    l=strg.swapcase()
    print(strg,l)
swap()
#
def reverse():
    strg=input('enter n:')
    r=int(input("value:"))
    print(strg * r)
    # print(strg[::-1])
reverse()
#
