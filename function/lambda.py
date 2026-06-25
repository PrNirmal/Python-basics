#lambda
[lambda x:x*3 if i%2==0 else 0 for i in range(10)]#DOUT
{lambda x:x*3 if i%2==0 else 0 for i in range(10)}

#
ad=lambda x,y:x+y+8
print(ad(1,2))
#
ad=lambda x,y,z:x+y+z
print(ad(1,2,1))
#
x=lambda a:a*10
print(x(5))
#
x=lambda a,b:a*b
print(x(2,4))
#
dict2={'square':lambda  x,y:x**y,'add':lambda x,y:x+y,'sub':lambda x,y:x-y}
sq=dict2['add']
# sq=dict2['square']
# sq=dict2['sub']
print(sq(2,3))
