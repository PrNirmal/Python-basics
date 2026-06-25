# strings are array
a = 'hello,world!'
# a[2]
print(a[2])
# looping through a string
for s in 'wednesday':
    print(s)
# check string using keyword 'in'
txt = 'she is a good girl'
print('is' in txt)
if 'is' in txt:
    print('iam good')
# using 'not in'keyword
txt = 'she is a good girl'
print('all' not in txt)
if 'all' not in txt:
    print('iam good')
# string concatenation,combine 2 strings using + operator
a = 'hello'
b = 'world'
# c=a+b
c = a + ' ' + b
print(c)
# slicing the string
a = 'hello,world'
print(a[2:5])
print(a[:5])
print(a[2:])
print(a[-5:-2])
# format,we cannot add numeric & character value,but using format its possible
age = 19
txt = 'my name is nirmal,iam' + age
print(txt)
# format method using placeholders{},we can concatenate int & char
age = 19
doorno = 11
phno = 2345
# txt='my name is nirmal,iam {}'
print(txt.format(age))
txt = 'doorno is {} and phno is {}'
# txt='doorno is {1} and phno is {0}'
print(txt.format(doorno, phno))
# ESCAPE CHARACTER '\'
# txt='we are 'student' from college'
txt = 'we are \"student\" from college'
print(txt)
# \n,\t,\r.\b,\\.\'
txt = 'hello\nworld'
txt = 'hello\tworld'
txt = 'hello\rworld'
txt = 'hello \bworld'  # erases 1 character space
txt = 'hello\\world'  # insert 1 backslash
txt = 'It\'s world'
print(txt)
# ex:
str4 = "abcd"
print(len(str4))

def string(str4):
    for i in range(len(str4)):
        # return str4[i]
        print(str4[i])
    for j in reversed(range(len(str4))):
        # return str4[j]
        print(str4[j])

string("abcd")

# print(str4[::i-1])
# print(str4(reversed[i]),'\n')
#
def findlen(str4):
    counter = 0
    for i in str4:
        counter += 1
    # print(counter)
    return counter


str4 = "abcd"
print(findlen(str4))
# hw
str5 = 'nirmal'
str5[:]
str5[::-1]
str5[:-1]
str5[:-2]
str5[:-3]
str5[:-4]
str5[:-5]
print(str5)

for i in range(len(str5)):
    print(str5[:i + 1])

for i in reversed(range(len(str5))):
    # print(i)
    print(str5[:i + 1])
# print(str5[::+1])
# print(str5[::+1])
# same word
list_1 = ["tree", 'fruit', 'apple', 'banana', 'furniture']
result = ''
prev_length = 5
for i in list_1:
    # print(i)
    # print(len(i))
    len_value = len(i)
    # if prev_length > len_value:
    #     result =i
    #     prev_length = len_value
    if prev_length == len_value:
        prev_length = len_value
        result = i
        print(result)
# large word
# list_1 = ["tree", 'fruit', 'apple', 'banana', 'furniture']
list_1 = ["tree", 'fruit', 'furniture', 'apple', 'banana']
result = ''
prev_length = 0
for i in list_1:
    # print(len(i))
    len_value = len(i)
    if prev_length < len_value:
        result = i
        prev_length = len_value
print(result)
# small word
list_1 = ["tree", 'fruit', 'apple', 'banana', 'furniture']
list_1 = ['fruit', "tree", 'apple', 'banana', 'furniture']  # 5>4(true)4 is not greater than of anything
result = ''
prev_length = 5
for i in list_1:
    # print(i)
    print(len(i))
    len_value = len(i)
    if prev_length > len_value:
        prev_length = len_value
        result = i
print(result)