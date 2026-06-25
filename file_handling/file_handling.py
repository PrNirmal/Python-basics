file = open("chsample1.json", 'r')
file.read()
file.close()
# os

# 1.abc-abstract base class
# 2.abort
import os

print('hello Frands')
os.abort()
print('hello Frands')
print('hello nanba')

import os
import shutil

main_path = "E:/code.txt"
despath = "D:/code.txt"
shutil.move(despath, main_path)
os.getcwd()
path = os.path.join()

path = "/home"
print(os.path.join(path, "Ajay", "file.txt"))

arr = map(int, input().split())
print(arr)

n = int(input("neg"))
x = 5
if x > n:
    print(x)
fist = sec = float('-inf')



n = float('-inf')
k = -2
if (n > k):
    print(n)
else:
    print(k)

for i in range(int(input())):
    print(i)
rec=[]
name="nl"
pame="cl"
sub_rec=list(name,pame)

if __name__ == '__main__':
    records=[]
    first=second=float('inf')
    for i in range(int(input())):
        name = input()
        score = float(input())
        sub_rec=[name,score]
        records.append(sub_rec)
    for i in records:
        if i[1]<first:
            second=first
            first=i[1]
        elif(i[1]<second and i[1]!=first):
            second=i[1]
    name=[]
    for i in records:
        if(i[1]==second):
            name.append(i[0])
    name_1=set(name)
    name_2=sorted(name_1)
    for win in name_2:
        print(win)

name_5=[1,2,3,4][2]

age,*name=input().split()

n=20.0
print("{:.2f}".format(n))
name="nk"
nk.split("")

import os

def sync_folders(original_folder, segmented_folder):
    # Get the list of files in both folders
    original_files = set(os.listdir(original_folder))
    segmented_files = set(os.listdir(segmented_folder))

    # Find the files that are in the original folder but not in the segmented folder
    files_to_delete = original_files - segmented_files

    # Delete the files in the original folder that do not have a corresponding segmented mask
    for file_name in files_to_delete:
        file_path = os.path.join(original_folder, file_name)
        os.remove(file_path)
        print(f"Deleted: {file_path}")

    print("Synchronization complete. The number of images in both folders should now be equal.")

# Example usage
original_folder_path = 'E:/Sorted Hard/Original_Images'
segmented_folder_path = 'E:/Sorted Hard/HardExudate_Masks'

sync_folders(original_folder_path, segmented_folder_path)

import os
original_path="E:/003"
audio_list=os.listdir(original_path)
for i in range(len(audio_list)):
    name=str(i+1).zfill(3)
    oldPath=os.path.join(original_path,audio_list[i])
    newPath=os.path.join(original_path,f"{name}")
    os.rename(oldPath,newPath)
print(os.listdir(original_path))

list_cap=['N']
list_odd=["3"]
list_small=['y']
list_even=["4"]
sorted_list=[i for j in [list_small,list_cap,list_odd,list_even] for i in sorted(j)]
print("".join(sorted_list))

list1=[]
for i in [list_small,list_cap,list_odd,list_even]:
    for j in sorted(i):
        list1.append(j)
print("".join(list1))
