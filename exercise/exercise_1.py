# 1 flames code
#func:
# def thecal(val,keyw):
#     thedel1 = val - keyw
#     if(thedel1>keyw):
#         thedel1=thecal(thedel1,keyw)
#     return thedel1

# val=18
# keyw="happyi"
# a=thecal(val,len(keyw))
# print(a)

name=input("Enter the name_1:")
name2=input("Enter the name_2:")

a=list(name)
b=list(name2)
# a=set(name).union(set(name2)) #as we dont want dupicates but the name char will also be deleted
for i in a:
    for j in b:
        if i==j:
            a.remove(i)
            b.remove(j)
            break
a.extend(b)
n=len(a)
keyw=["F","L","A","M","E","S"]
# for i in range(5):
#     val=len(a)
#     thedel=thecal(val,len(keyw))
#     keyw=keyw.replace(keyw[thedel-1],"")
val=1
global l
while(val):
    for i in range(n):
        i=i%len(keyw)
        l=keyw[i]
    if len(keyw)!=1:
        keyw.remove(l)
    if len(keyw)==1:
        print(l)
        val=0
if keyw=="F":
    print("The relationship :Friends")
elif keyw=="L":
    print("The relationship :Love")
elif keyw=="A":
    print("The relationship :Affection")
elif keyw=="M":
    print("The relationship :Marriage")
elif keyw=="E":
    print("The relationship :Enemy")
else:
    print("The relationship :Son")
