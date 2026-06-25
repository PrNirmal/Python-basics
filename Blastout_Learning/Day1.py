# String
x="Nirmal"
y='ajay'
z="""Nirmal is hungry"""
print(z)
print(x)
print(y)


# int
x=-10
type(x)

name="Nirm al"
name[4]
# N:0,I:1,r:2,m:3,a:4,l:5

# strinf slicing
name="Vishal"
name[0:4]
name[0:]
name[:6]
name[:4]
name[::-1]
print(name.count("i"))
print('Nirmal\'s')

name="Hello welcome welcome {fname}  to python,{kname} welcome "
print(name.find("come"))
print(name.replace("welcome","happy",0))
print(name)
name1=name.replace("welcome","happy")
# name[-6]
print(name+name1)

name.format(fname="buddy",kname="say")

print(f"{name} hello")
dir(name)
type(name)
len(name)

x=3.66
print(round(x,1))

# Day 2

name="0.5"

name.isalnum()

name2="vishal"

name2.ljust(5,"o",)


name2.ljust(4,"0")

name2="Chandra akka akka coding Chandra"

name2.strip("Chandra")
# name2.replace("akka","")
name2.lstrip("Chandra")
name2.rstrip("Chandra")

name3="vishaka and chandra chandra  and are sisters"

name3.rpartition("chandra")