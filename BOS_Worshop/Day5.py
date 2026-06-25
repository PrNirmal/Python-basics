# file read
file_1=open("C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/sample3.txt")
print(file_1.read())
file_1.close()

file_1=open("C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/sample1.txt","w")
print(file_1.write("hello"))
file_1.close()

file_2=open("C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/sample.txt","r+")
file_2.write("\nThe file file is replaced")
print(file_2.read())
file_2.close()

file_3=open("C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/sample3.txt","w+")
file_3.write("File 3 is created")
file_3.read()
file_3.write("File 3 is replaced")
print(file_3.read())


file_4=open("C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/sample3.txt","a+")
file_4.read()
file_4.close()
file_4.write("A text is added")
file_4.read()


with open("C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/sample3.txt","r") as file:
    lines=file.readlines()

for line in lines:
    print(line)

with open("C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/sample3.txt","r") as file:
    for line in file:
        print(line)

# import

import os

file_path="C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/sample3.txt"

if os.path.exists(file_path):
    with open(file_path,"r") as file:
        lines=file.readlines()
        for line in lines:
            print(line)
else:
    print("The file doesn't exists")

# moving file

import os
import shutil

path="C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/"
file_path="C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/sample.txt"
dir_path="C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/folder_1"
os.makedirs(dir_path)
shutil.move(file_path,dir_path)
# delete
# os.rmdir(dir_path)
dir_name=os.path.join()
dir_path="C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/folder_1"
for i in range(1,6):
    file_path=f"C:/Users/prnir/PycharmProjects/pythonProject/BOS_Worshop/Day{i}.py"
    shutil.move(file_path,)
os.removedirs(dir_path)

# file
remove_file=os.listdir(dir_path)
for file in remove_file:
    filename=os.path.join(dir_path,file)
    os.remove(filename)
os.removedirs(dir_path)