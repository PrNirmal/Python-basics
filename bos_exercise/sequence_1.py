# # # list,tuple,dict,set,string
# # # List is mutable,indexed,ordered,allows duplicate

# # # string is immutable,indexed,ordered,allows duplicate

# # from turtle import st


# # names=["Nirmal","ajay",123,32,32]
# # names[0]="Vijay" #mutable
# # print(names)

# # # print(names[5])  #index error how can to handle this error !!


# # names=["Nirmal","ajay",123,32,32]
# # names.append("jai")
# # # names
# # names.reverse()
# # print(names)

# # # tuple
# # # immutable,indexed,ordered,allows duplicate

# # # tuple_1=tuple()
# # tuple_2=('2',3,5,3,2,2,3,3)
# # tuple_2[1]=10

# # tuple_2.count(3)
# # tuple_2.index(3,4,5)
# # # dir(tuple)
# # # dir(())



# # # join strip

# # sentence=" Nirmal is the class leader "
# # # sentence.strip(" Nrie")


# # # 1) sentence- remove empty space from front and back
# # # 2) nirmal-is-...........

# # # sentence=sentence.strip().split(" ")
# # # print(sentence)
# # # sentence=sentence.split(" ")
# # # print(sentence)
# # # "-".join(sentence)
# # "-".join(sentence.strip().split(" "))


# # name="nirmal"
# # ajay=name.maketrans("a","c")
# # name.translate(ajay) 




# # print("nirmal")
# # for i in "nirmal":
# #     print(i,end="")

# # n=1


# # list_1=[1,2,3,4,5]

# # for i in list_1:
# #     print("Element:{0},index:{1}".format(i,list_1.index(i)))



# # for idx,ele in enumerate(list_1,1):
# #     print(idx,ele) 





# # # calculator for +-*/,continue



# # # user input->3, next continue or no

# # Continue=True
# # while Continue:
# #     num_1=int(input("Enter first number:"))
# #     nume_2=int(input("Enter second number:"))
# #     operator=input("Enter operator:")

# #     if operator=="+":
# #         print(num_1+nume_2)
# #     elif operator=="-":
# #         print(abs(num_1-nume_2))
# #     elif operator=="*":
# #         print(num_1*nume_2)
# #     elif operator=="/":
# #         print(num_1/nume_2)
# #     else:
# #         print("Invalid operator")
    
# #     Continue=input("Do you want to continue?(yes/no)")=="yes"




# # # function defeinition
# # def check_the_color():
# #     print("test color")

# # # function calling
# # check_the_color()

# # # formal parameter
# # def addition(num_1=10,num_2=0):
# #     print(num_1+num_2)


# # addition(num_2=20)

# # # postitional argument
# # addition(10,32)

# # # keyword argument
# # addition(num_2=10,num_1=32)

# # # positional argument and keyword argument
# # addition(10,num_1=32)
# # addition(num_1=32,num_2=10)






# # def name():
# #     print("Nirmal")

# # name() #function calling



# # def digit_count(num):

# #     if num<10:
# #         return 1
# #     else:
# #         return  1 + digit_count(num//10)
# # # num=12345

# # digit_count(12345)



# # # num 12345

# # # 1 + (12345//10)
# # #     1+(1234//10)   
# # #       1+(123//10)
# # #  
        




# # # 

# # # palindrome true? false:

# # def ispalindrome(value):

# #     if len(value)<=1:
# #         return True

# #     # pass
# #     if value[0]!=value[-1]:
# #         return False
    
# #     return ispalindrome(value[1:-1])


# # ispalindrome("madam")
# # # madan
# # # nadam


# # # break,continue,pass


# # # packing and unpacking


# # # packing
# # a=[1,2,3,4]
# # a,b,c,d=[1,2,3,4]
# # print(a)
# # print(b)


# # def print_list(**args):
# #     print(args)

# # print_list(name="nirmal",age=18)




# # a,*b,c,d=[1,2,3,4,5]


# def print_list(args):
#     print("print args:", args)

# # print_list([1,2,3,4,5])


# # /,* 
# # /position only argument
# # *keyword only argument

# # argument separators
# def fruits(a,/,b,*,c,d,e):
#     print(a,b,c,d,e)


# fruits("apple","banana",c="orange",d="pineapple",e="berry")
    
# # def :
#     # print("print args:", args)

# # import typing
# def char_count(name:int|float,letter:str)->int:
#     # print(name.count(letter))
#     # print(name,letter)
    
#     return "nirmal"



# name="nirmal"
# char_count("nirmal",20)
# # char_count(name,"n")








# # Student Result Management System:
# # Problem Statement:
# # Create a program using the following functions:
# # Required Functions:
# # get_marks() → Takes marks for 5 subjects from user (handle invalid input).

# def get_marks():
#     marks_list=[]
#     for i in range(5):
#         try:
#             mark=int(input("Enter A mark for subject"))
#             if 0<=mark<=100:
#                 marks_list.append(mark)
#             else:
#                 raise ValueError("Marks must be between 0 and 100.")
#         except ValueError as e:
#             print("Invalid input:", e)
#     return marks_list

# # calculate_average(marks_list) → Returns average.

# def calculate_average(marks_list):
#     return sum(marks_list)/len(marks_list)


# # assign_grade(avg) → Returns grade (A/B/C/Fail).
# def assign_grade(avg):
#     if avg>=90:
#         return "Grade: A"
#     elif avg>=80:
#         return "Grade: B"
#     elif avg>=60:
#         return "Grade: C"
#     else:
#         return "Grade: Fail"

# # display_result(total, avg, grade) → Prints final result.4

# def display_result(mark_list ,avg):
#     print("Total Marks:", sum(mark_list))
#     print("Average Marks:", avg)
#     print(assign_grade(avg))


# get_marks_list=get_marks()
# avg=calculate_average(get_marks_list)
# display_result(get_marks_list,avg)


# # Problem 2: ATM System Using Functions
# # Problem Statement:
# Initial_balance = 10000


# # Required Functions:
# # deposit(balance)
# def deposit():
#     global Initial_balance
#     val=True
#     while val:
#         try:
#             amount=int(input("Enter amount to deposit:"))
#             if amount>0:
#                 Initial_balance+=amount
#                 val=False
#             else:
#                 raise ValueError("Deposit amount must valid")
        
#         except ValueError as e:
#             print("Invalid input:", e)
            
# # deposit()

# # withdraw(balance)

# def withdraw():
#     global Initial_balance
#     val=True
#     while val:
#         try:
#             amount=int(input("Enter amount to withdraw:"))
#             if amount>0 and amount<=Initial_balance:
#                 Initial_balance-=amount
#                 print("Withdrawal successful{}. Current balance: {}".format(amount,Initial_balance))
#                 val=False
#             else:
#                 raise ValueError("Insufficient balance")
#         except ValueError as e:
#             print("Invalid input:", e)

# # check_balance(balance)

# def check_balance():
#     global Initial_balance
#     print("Current balance:", Initial_balance)



# # atm_menu() → Shows menu

# def atm_menu():
#     print("ATM Menu:")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")
#     return int(input("Select an option (1-4):"))


# # main() → Controls program using while loop

# def main():
#     while True:
#         option=atm_menu()
#         # if option==1:
#         #     deposit()
#         # elif option==2:
#         #     withdraw()
#         # elif option==3:
#         #     check_balance()
#         # else:
#         #     print("Exiting ATM. Thank you!")
#         #     break
#         match option:
#             case 1:
#                 deposit()
#             case 2:
#                 withdraw()
#             case 3:
#                 check_balance()
#             case 4:
#                 print("Exiting ATM. Thank you!")
#                 break
          
# main()

# # Rules:
# # Handle non-numeric input.
# # Prevent over-withdrawal.
# # Exit only when user selects option 4.



# file=open("BOS_Worshop\sample3.txt","r")
# content=file.read()
# file.close()


# with open("BOS_Worshop\sample3.txt","r") as file:
#     content=file.read()



# # input dict -> name of the student and list of his marks
# # {"Nirmal":[90,80,70,90,20],"ajay":[80,70,60,90,20]}

# # file handling
# # stutent.txt=> 
# # Nirmal:90,80,70,90,20
# # ajay:80,70,60,90,20


# # Json --> java script object notation

# dict_1={"Nirmal":[90,80,70,90,20],"ajay":[80,70,60,90,20]}
# type(dict_1)

import json

# a=json.dumps(dict_1) #python object to json string -> serialization
# print(a)
# print(type(a))
# # "{"Nirmal": [90, 80, 70, 90, 20], "ajay": [80, 70, 60, 90, 20]}"

# # json to python object
# b=json.loads(a) #json string to python object -> deserialization
# print(b)
# print(type(b))

sample_dict={
    "name":"nirmal",
    "age":18,
    "is_student":True,
    "address":{
        "street":"123 Main St",
        "city":"Anytown",
        "state":"CA",
        "zip":"12345"
    },
    "married":False,
    "Children":None,
    "marks":[90,80,70,60,50],
    "Hobby":("read","write"),
    "weight":70.5
}

sample_json=json.dumps(sample_dict)
print(sample_json)

# python        Json
# dict         object  
# list         array
# tuple        array
# string       string
# int          number
# float        number
# True        true  
# False       false
# None         null


# dump, load

# dumps -> string
# loads -> python object

# with open("bos_exercise\check.json","w") as file:
#     json.dump(sample_dict,file)

# with open("bos_exercise\check.json","r") as file:
#     data=json.load(file)

# print(data)

import pickle

# data={"name":"nirmal","age":18,"is_student":True}

# pickle.dump(data,open("bos_exercise\check.pkl","wb"))
pickle.load(open("bos_exercise\check.pkl","rb"))