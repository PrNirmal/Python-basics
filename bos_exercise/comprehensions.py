# list, tuple, set, dict
# list, dict, set

list_1=[1,2,3,4,5]
list_2=[]
for i in list_1:
    if i%2==0:
        list_2.append(i)
print(list_2)

list_2=[x for x in list_1 if x%2==0]

square_list=[x**2 for x in range(1,11)]


set_comprehension={x**2 for x in range(1,11)}

# {key:value}

dict_comprehension={f"Square_{x}":x**2 for x in range(1,11) if x%2==0}



names=["nirmal","ajay","jai","nirmal","nirmal","nirmal","nirmal","nirmal"]

names_set=set(names)
names_set_comprehension={name for name in names}



dict_1={"nirmal":20,"ajay":25,"jai":30}
dict_1.items()
result={name:"Pass" if marks>=25 else "Fail" for name,marks in dict_1.items()}



list_1=[1,2,3,4,5]
list_2=[9,8,7,6,5]

result={(x,y) for x in list_1 for y in list_2}

# list_3=set()
# for i in list_1:
#     for j in list_2:
#         list_3.add((i,j))

words=["nirmal","ajay","jai"]

result={char for word in words for char in word}


import datetime
n=[(2019,2,1),(2019,2,1),(2019,2,1)]
x=datetime.datetime(*n[0])
print(x.strftime("%A"))
x=["Friday","Monday"]