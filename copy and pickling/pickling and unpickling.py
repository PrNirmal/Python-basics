# pickling
#pickle.dump()#only writes
#pickle.dumps()  # for no of objects for string
# unpickling
#pickle.load()#only reads
#pickle.loads()  # unpicking those objects


# 2 student name pickle and unpicle stu1={name:}

#2 dic{name,age course,dis}-1 like wise student 2(pic and unpick)

#5 students dic{name,class,subject} (hint shallow copy and deepcopy)

import pickle
import sys

stu1={"name":"nirmal"}
stu2={"name":"gokul"}
list_1=[stu1,stu2]
for i in range(len(list_1)):
    file=open("file","wb")
    pickle.dump(list_1[i],file)#pickling
    file.close()
    file=open("file","rb")#unpickling
    s=pickle.load(file)
    file.close()
    print(s)
#2.
stu1={"name":"nirmal","degree":"be","age":"19","dept":"cse"}
stu2={"name":"gokul","degree":"bsc","age":"19","dept":"cs"}
list_1=[stu1,stu2]
for i in range(len(list_1)):
    file_1=open("file1","wb")
    pickle.dump(list_1[i],file_1)#pickling
    file_1.close()
    file_1=open("file1","rb")#unpickling
    s=pickle.load(file_1)
    file_1.close()
    print(s)

#3
import pickle
stu1={"name":"nirmal","degree":"be","mark1":35,"mark2":40,"mark3":50}
stu2={"name":"gokul","degree":"bsc","mark1":50,"mark2":88,"mark3":70}
stu3={"name":"ravi","degree":"bsc","mark1":98,"mark2":23,"mark3":44}
stu4={"name":"ram","degree":"bsc","mark1":22,"mark2":45,"mark3":55}
stu5={"name":"raj","degree":"bsc","mark1":25,"mark2":55,"mark3":65}
list_2=[stu1,stu2,stu3,stu4,stu5]
for i in range(len(list_2)):
    file_2=open("file2","wb")
    pickle.dump(list_2[i],file_2)#pickling
    file_2.close()
    file_2=open("file2","rb")#unpickling
    s=pickle.load(file_2)
    file_2.close()
    print(s)

#eg problem:
import pickle
a={"name":"nir"}
b={"name":"gok"}
file=open('my file','wb')
pickle.dumps(a,file)
pickle.dump(b,file)
file.close()
file=open("my file","rb")
x=pickle.load(file)
file.close()
print(x)


s=[7,7]
sys.getsizeof(s)



import pickle
def fruits():
    a="apple"
    b="banana"
    c="orange"
    print(a)
l=pickle.dumps(fruits)
k=pickle.loads(l)
fp=open("hello","wb")
fp.write(l)
fp.close()
f=open("hello","rb")
print(b)
f.close()