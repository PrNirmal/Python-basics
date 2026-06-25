# list comprehensions(creating new list from existing list)
list_1=list()
for i in range(10):
    if i%2==0:#even no divisibleby2 and remaindr 0
        # print(i)
        list_1.append(i*3)
    else:#dout
        list_1.append(0)
print(list_1)
#
list_1=[i*3 for i in range(10) if i%2==0]#for i in range if condition
list_1=[i*3 if i%2==0 else 0 for i in range(10)]
print(list_1)
#
numbers=[1,2,3,4,5]
squares=[]#outputlist
for i in numbers:
    squares.append(i**2)#outputlist.appendof outputexpression
print(squares)
# inputlist=numbers,outputexpression=i**2,variable(i)represents the element of list(numbers).
numbers=[1,2,3,4,5]
squares=[i**2 for i in numbers]
print(squares)