fruit="banana"
mylist=iter(fruit)
next(mylist)
mylist.__next__()

# yield-generator keywork

def fruit_1(x):
    for i in range(len(x)):
        k=m[i]
        yield k
m="banana"
a=fruit_1(m)
for i in range(len(m)):
    print(a.__next__())


m=[1,2,3,4,"nirmal"]
f_iter=iter(m)
f_iter.__next__()
for i in range(len(m)-1):
    print(next(f_iter))
for i in range(len(m)):
    if type(m[i])==str:
        l=iter(m[i])
        print(next(l))
        for i in range(len(m[i])-1):
            print(l.__next__())

def for_list():
    n=[1,2,3,"nirmal"]
    yield n

l=for_list()
n=iter(l)
next(l)

def for_list1():
    n = [1, 2, 3, "nirmal"]
    for i in range(len(n)):
        yield n[i]
        if type(n[i])==str:
            k=n[i]
            for m in range(len(k)):
                yield k[m]
        i+1
a=for_list1()
k=iter(a)
next(k)

dict_1={"name":"nirmal","age":19}
l=dict_1.values()
print(l)
n=iter(l)
next(n)
# monkey patching,recursive function,decorator
