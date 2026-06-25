# for while

# for
# initialising

# while condtion false


for i in range(10):
    print(i,end=" ")

i=0
while (i<10):#10
    print(i,end=" ")
    i+=1
# print()


# Print Triangle star
# Input: N = 9
# Output:
#           *
#          * *
#         * * *
#        * * * *
#       * * * * *
#      * * * * * *
#     * * * * * * *
#    * * * * * * * *
#   * * * * * * * * *

number=int(input("Enter No of Lines"))

# for loop
# for i in range(1,number+1):
#     print(" "*(number-i)+"* "*i)

# while loop

i=1
while i<=number:
    print(" "*(number-i)+"* "*i)
    i+=1


fruits=["apple","banana","grapes"]
for fruit in fruits:
    print(fruit)

i=0
while i<len(fruits):
    print(fruits[i])
    i+=1

# using conditions in loop

fruits=["banana","apple","mango"]
for fruit in fruits:
    if fruit=="banana":
        print("Its yellow in color")
    elif fruit=="apple":
        print("Its Red in color")
    else:
        print("Other color")


# break and continue

numbers=list(range(2,10))

for number in numbers:
    if number==6:
        continue
    print(number)
    # else:
    #     print(number)


# nested loop

fruits_1=["apple","mango","banana"]
fruits_2=["berry","cherry","orange"]

for i in fruits_1:#banana
    for j in fruits_2:#berry
        print(i,j)

# def
# function declaration
def print_name(name):
    print(name)

# function calling
print_name("nirmal")

def calculator(operator,input1,input2):
    if operator=='+':
        print(input1+input2)
    elif operator=='-':
        print(input1-input2)
    elif operator=='*':
        print(input1*input2)
    elif operator=='/':
        print(input1/input2)
    else:
        print("Enter a valid operator")

flag="yes"
while (flag=="yes"):
    operator=input("Enter the operator(+,-,*,/):")
    input1=int(input("Enter input 1:"))
    input2=int(input("Enter input 2:"))
    if operator=='+':
        print(input1+input2)
    elif operator=='-':
        print(input1-input2)
    elif operator=='*':
        print(input1*input2)
    elif operator=='/':
        print(input1/input2)
    else:
        print("Enter a valid operator")
    flag=input("Do you want to continue if yes")

for i in range(1,10):
    print(i,end="")
name="NIrmal"
name[::2]



