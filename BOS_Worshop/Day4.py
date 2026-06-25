# functions

# def
# reusable code to avoid repetation of code

def printable_func(statement):
    print(statement)

# printable_func("nirmal")


# # lambda function
# x=lambda a:a+5
# print(x(5))
# type(x)

# y=lambda a,b:a+b
# print(y(45,6))

# # lambda given number odd or even

# z=lambda x:"Even" if x%2==0 else "Odd"
# print(z(2))

# # Basic List comprehension

# list_1=["apple","banana","orange","pineapple","berry","cherry"]
# list_2=[]

# for fruit in list_1:
#     if "a" in fruit:
#         list_2.append(fruit)

# print(list_2)


# # List Comprehension
# list_1=["apple","banana","orange","pineapple","berry","cherry"]

# list_2=[fruit for fruit in list_1 if "a" in fruit]
# list_2

# # 1 - 100 even number => list

# list_3=[num for num in range(1,101) if num%2==0]
# list_4=[num for num in range(2,101,2)]


# # exception handling

# list_5=[1,2,3,4]
# list_5[6]

# # Nameerror

# print(5/0)

# # try except

# try:
#     a=5
#     print(a/0)
# except ZeroDivisionError as e:
#     print(e)

# list_5=[1,2,3,4]
# try:
#     print(list_5[7])
# except IndexError as e:
#     print(e)
# else:
#     print("No Error")
# finally:
#     print("Exception executed")


