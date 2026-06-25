#for loop(){
# statements
# }
var_1=1
var_2=2
var_3=3
if var_1==1:
    print(1)
    if var_2==2:
        print(4)
        if var_3==3:
            print(5)
print('ram')
#
for i in range(10):
    print(1)
    # print(i)
# print('i')
    print('a')
    print(i,'i')
    print(i,'a')
# 3*2 concept loop iterate
for i in range(3):
    print('a')
    for j in range(2):
        print('second loop')
        for k in range(2):
            print('loop')
# while
counter=0
# while False:
while True:
    print(counter)
    counter = counter + 1
    if counter==10:
        break
# for loop indexing using enumerate
# list__=[3,2,9,8]
# for idx in range(len(list__)):
    # print(list__[idx])
# for idx in enumerate(list__):
    # print(idx)
# for idx in range(len([5,7,8,7])):can't access directly list in forloop by using range,but by enumerate..
for idx in enumerate([5,7,8,7]):
    print(idx)
var = 'a'
for idx in enumerate(range(10)):
    # print(idx,var)
    # print(idx,'a')
    print(idx)
    # print('a')
#my work
#indentation
if 5>2:
 print('greater')
#
if 3>1:
    print("greater")
    print("greater")
#
if 3>1:
    print('greater')
if 2>1:
    print('greater')
#
if 1<2:
    print('hi')
else:
    print('ok')
print('all')
#



