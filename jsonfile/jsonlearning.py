# for json to python file-loads
# for python to json - dumps(intent=2) for perfect
# using dumps as we using in string format
# syntax a=json.dump
# json-javascript object notation
import json

# update,del +modify
# trunk
# url to file then to json and to python file
# python-json
# dict-Object
# list-Array
# tuple-Array
# str-String
# int-Number
# float-Number
# True-true
# False-false
# None	null

dict1 = '''{
    "fruit": "Apple",
    "size": "Large",
    "color": "Red"
}'''
print(dict1)
s = json.loads(dict1)
s.update({'Number': 2})
print(s)
print(json.dumps(s, indent=2))

# sample 1 file
import json

with open("sample1.json") as fp:
    s = json.load(fp)
s.update({'Number': 2})  # update operation
del (s['fruit'])  # delete operation
with open("chsample1.json", 'w') as f:
    json.dump(s, f, indent=2)
# to change the original fie

with open("chsample1.json", 'w') as f:
    json.dump(s, f, indent=2)

# sample 2:

import json

with open("sample2.json") as kp:
    s=json.load(kp)

k=s["address"]
k.update({"homeNo":23})
del(k["city"])
l=s["phoneNumbers"]
l.append({"owner":"no yet fixed","age":"don't know"})

with open("chsample2.json","w") as kpk:
    json.dump(s,kpk,indent=2)


# sample 3:
import json

with open("sample3.json") as file:
    new=json.load(file)
add={}
thelist1=[]
thelist2=[]

for i in range(len(new)):
    k=new[i]
    thelist1.append(k["color"])
    thelist2.append(k["value"])
add["alcol"]=thelist1
add["vlcol"]=thelist2
new.append(add)
noitem=len(new)
new.append({"noofitems":noitem})

with open("chsample3.json","w") as kpip:
    json.dump(new,kpip,indent=2)


# sample 4:
import json

with open("sample4.json") as fpop:
    newf=json.load(fpop)

anew=newf["people"]
len(anew)
# name1="ragu"
# name2="ram"
# name3="raju"
# i=1
for accdict in anew:
    del(accdict["firstName"])
    # newname='{name}'
    newname=input("enter the name")
    accdict.update({"thename":newname})
    # i+=1

with open("chsample4.json","w") as npop:
    json.dump(newf,npop,indent=2)

