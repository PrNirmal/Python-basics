# Dictionaries are used to store data values in key:value pairs
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates

thisdict={"brand":"ford","model":"mustard"}
print(thisdict)
thisdict["year"]=2007
print(thisdict)

# clear
student={"name":"nirmal","dept":"be"}#used to clear the dict
print(student.clear())#make it as a empty dictionary

# copy
student={"name":"nirmal","dept":"be"}#used to copy the dict
student_2=student.copy()
print(student_2)

# fromkeys
#The fromkeys() method returns a dictionary with the specified keys and the specified value
# syntax-dict.fromkeys(keys, value)
x=('key1','key2')
print(dict.fromkeys(x))#defult the values will be assigned as none
y=0
print(dict.fromkeys(x,y))
y=[1,2]
print(dict.fromkeys(x,y))#it will only store one value to all the keys

#get
dict_1={'one':'apple','two':'orange','three':'mango'}
dict_1.get('one')#The get() method returns the value of the item with the specified key.
dict_1.get('apple',"not found")#(keyname,value)Optional. A value to return if the specified key does not exist. Default value None
dict_1.get('two','not found')

#items
dict_1={'one':'apple','two':'orange','three':'mango'}
dict_1.items()# A view object that displays a list of a given dictionary’s (key, value) tuple pair
student={"name":"nirmal","dept":"be"}
student.items()

# keys
student={"name":"nirmal","dept":"be"}#used to get the keys of the dictionary
print(student.keys())#A view object is returned that displays all the keys.
# This view object changes according to the changes in the dictionary.
for i in student.keys():
    print(i)

# pop
student={"name":"nirmal","dept":"be","age":19}
student.pop("dept")#used to pop the key and value mentioned
print(student)
student.pop("name")
print(student)

# popitem
student={"name":"nirmal","dept":"be","age":19}#pop item will pop the last key and value pair
student.popitem()#this will pop the last item-{"name":"nirmal","dept":"be"}--this is the dict after popitem
student.popitem()#this will pop the last item-{"name":"nirmal"}--this is the dict after popitem
print(student)

# setdefault
student={"name":"nirmal","dept":"be","age":19}
student.setdefault('name','raj')#it will check whether the key is present or not if the key is found the return its value
print(student)
student.setdefault('course','cse')#else return the value passed and will store the keyitem as kaey value pair in the dict
print(student)

# update
student={"name":"nirmal","dept":"be","age":19}
student.update({"language":"python"})#used to update a new key and value pair at the end
print(student)
student.update({"language":"java"})#it is used to update an existing key and value with new value
print(student)

# values
student={"name":"nirmal","dept":"be","age":19}
print(student.values())#used to get the values of the dict


# dict
# dict1={}/to create
# dict1=dict()/to create
dict={"India":"delhi"}
dict["India"]
# print(dict)
# x=dict.get("India")
# print(x)
dict1={"India":"delhi","ram":([1,2,5,7,9],[4,5,6,7])}
# dict1.items()
print(dict1)
# print(len(dict1))
dict1['ram'][0][1]
dict1['ram'][1][2]
dict1.update({"mal":"one"})
dict1["zero"]="corner"#update
# dict1.pop('h')
print(dict1)
# setdefault
dict1.setdefault('kav','not found')
print(dict1)
# dict1.update({'lang':'py'})
dict1.update({'apple':'fruit'})
dict1.setdefault('anu','zero')
dict1.get('one','two')
dict1.setdefault('one','two')
# hw "key_3":":"
dictionary={"key_1":[1,3,4],"key_2":["one","three","four"]}
# print(dictionary.items())
# b=['key_2']
for i in dictionary:
    print(dictionary[i])
    for j in dictionary[i]:
        print(j)
for i,j in dictionary.items():
    print(i,j)
    print(i,' : ',j[0])
    print(i,' : ',j[1])
    print(i,' : ',j[2])
    # for a in range(len(j)):
        # print(j[a])
#
dictionary={"key_1":[1,3,4],"key_2":["one","three","four"]}
for i,j in dictionary:
    print(i,j)

# n=['one','three','four']
# dictionary.get('key_1')
# (dictionary.get('key_2'))
print(i)
# loop
student1={"name":"nirmal","dept":"be","age":19}
for i in student1:
    # for i in student1.values():
    # for i in student1.keys():
    #     for i in student1.items():
    #     for i,j in student1.items():
            # print(i)
            # print(i,j)
    print(i)
    print(student1[i])
# del a particular keyvalue
animal={'rabbit':'carrot','deer':'grass'}
del animal['deer']
# del animal
print(animal)