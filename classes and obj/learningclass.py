class student:
    pass
stu1=student()
stu2=student()

stu1.name="nirmal"
stu1.rno=29

stu2.name="ravi "
stu2.rno=89
print(stu1.name)# this will take more code so the conclusion is.....


from datetime import date


class Student:
    ad = 1
    def __init__(self, name, roll, dob, city):  # method1
        print("Working")
        self.name = name  # for instance variable
        self.dob = dob  # attributes
        self.roll = roll
        self.city = city

    # @classmethod
    # def address(cls):  # method2
    #     addr = f'name:{self.name}\nDob:{self.dob}\ncity:{self.city}'
    #     return addr
    #
    # @staticmethod
    # def age():
    #     current_year = date.today().year
    #     return current_year - self.dob


stu1=Student("nirmal",23,2004,"chennai")
stu2=Student("raj",25,2023,"kaarai")
print(stu1.name)
print(stu1.roll)
# print(stu1.address())
# print(stu2.address())
# print(stu1.age())#this how it works
# student.age(stu1) so we have to pass argument stu1


class Student:
    name=None
    tamil=None
    english=None
    maths=None
    science=None
    social=None
    def calculate_total(self):
        total_1=self.tamil+self.english+self.maths+self.science+self.social
        print(f'The total of the student {total_1}')
        # self.total=total_1

# stu1=Student()
# stu1.name='raj'
# stu1.tamil=10
# stu1.english=20
# stu1.maths=30
# stu1.science=40
# stu1.social=50
# stu1.total()

stu2=Student()
stu2.name='ram'
stu2.tamil=30
stu2.english=30
stu2.maths=30
stu2.science=10
stu2.social=10
stu2.calculate_total()




class Nirmal():
    # @staticmethod
    def __init__(self,fname):
        self.name=fname
    name="nir"
    def welcome(self,name):
        print(name)
    def age(self):
        print(self.name)
    @classmethod
    def classcheck(cls):
        print(cls.name)


p1=Nirmal("nirmal")
p1.name
p1.classcheck()
p1.age()
p1.welcome("nirmal")
p1.age("12")
p2=Nirmal("ajay")
p2.name



class StudentRecord:
    name="ajay" #class variable

    def printer(self,name):
        print("hello world",name)

record_1= StudentRecord() #instance of the class 1
record_2= StudentRecord() #instance of the class 2

# record_1.name

record_1.printer("nirma")
record_2.printer("ajay")
record_2.name
record_2.name="nirmal"
record_2.name
record_1.name


class StudentRecord:
    __check="ajay" #class variable

    def __init__(self,name,age):
        self.__name=name #instance variable
        self.age=age

    def __printer(self):
        print("hello world",self.__name)
    
    def checker(self):
        self.__printer()

    @classmethod
    def classcheck(cls):
        print("hello world",cls.__check)

    @staticmethod
    def age_print(name):
        print("hello world",name)

record_1= StudentRecord("nirmal",19) #instance of the class 1
record_1.__name
record_1.checker()

# StudentRecord.__check

# polymorphism

class Animal:
    def speak(self):
        print("Animal speaks")

class Bird:
    def speak(self):
        print("Bird speaks")


a=Animal()
b=Bird()
a.speak()
b.speak()


# inheritance
# 1) single inheritance, multiple inheritance, multilevel inheritance, hierarchical inheritance, hybrid inheritance

class Parent:
    def parent_method(self):
        print("This is a parent method")

class Child(Parent):
    def child_method(self):
        print("This is a child method")

c=Child()
c.parent_method()
c.child_method()


# multiple inheritance

class Father:
    def father_method(self):
        print("This is a father method")

class Mother:
    def mother_method(self):
        print("This is a mother method")

class Child(Father,Mother):
    def child_method(self):
        print("This is a child method")

c=Child()
c.father_method()
c.mother_method()
c.child_method()

# multilevel inheritance

class Grandparent:
    def grandparent_method(self):
        print("This is a grandparent method")

class Parent(Grandparent):
    def parent_method(self):
        print("This is a parent method")

class Child(Parent):
    def child_method(self):
        print("This is a child method")

e=Child()
e.grandparent_method()

# hierarchical inheritance

class Parent:
    def parent_method(self):
        print("This is a parent method")
    
class Child1(Parent):
    def child1_method(self):
        print("This is a child1 method")

class Child2(Parent):
    def child2_method(self):
        print("This is a child2 method")

# hybrid inheritance

class Grandparent:
    def grandparent_method(self):
        print("This is a grandparent method")

class Mother(Grandparent):
    def mother_method(self):
        print("This is a mother method")

class Father(Grandparent):
    def father_method(self):
        print("This is a father method")

class Child(Mother,Father):
    def child_method(self):
        print("This is a child method")



# abstraction
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        print("This is a rectangle")

shape=Rectangle()
shape.area()


# method overriding

class Parent:
    # name="nirmal"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def method(self):
        print("This is a parent method")

class Child(Parent):
    def __init__(self,address,name,age):
        super().__init__(name,age)
        self.address=address

    def method(self):
        print(self.name)
        print(self.age)


c=Child("nirmal", 19,"chennai")
c.method()
