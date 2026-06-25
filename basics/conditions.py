# conditions.py

# 1. Simple if statement
x = 10
if x > 5:
    print('x is greater than 5')  # Executes if x is greater than 5

# 2. if-else statement
y = 3
if y % 2 == 0:
    print('y is even')  # Executes if y is even
else:
    print('y is odd')   # Executes if y is not even

# 3. if-elif-else statement
z = 0
if z > 0:
    print('z is positive')  # Executes if z is greater than 0
elif z < 0:
    print('z is negative')  # Executes if z is less than 0
else:
    print('z is zero')      # Executes if z is exactly 0

# 4. Nested if statement
a = 7
if a > 0:
    if a < 10:
        print('a is a positive single-digit number')  # Executes if a is between 1 and 9

# 5. Ternary conditional operator
b = 8
result = 'even' if b % 2 == 0 else 'odd'  # Assigns 'even' if b is even, otherwise 'odd'
print(f'b is {result}')

# 6. Multiple conditions with 'and' and 'or'
c = 15
d = 20
if c > 10 and d > 10:
    print('Both c and d are greater than 10')  # Executes if both conditions are True
if c > 10 or d < 10:
    print('At least one condition is True')    # Executes if either condition is True

# 7. Using 'not' in conditions
e = False
if not e:
    print('e is False')  # Executes because e is False

# 8. Checking membership with 'in' and 'not in'
fruits = ['apple', 'banana', 'cherry']
if 'banana' in fruits:
    print('banana is in the list')  # Executes if 'banana' is found in the list
if 'orange' not in fruits:
    print('orange is not in the list')  # Executes if 'orange' is not found in the list

# 9. Comparing strings
name = 'Alice'
if name == 'Alice':
    print('Hello, Alice!')  # Executes if name matches 'Alice'

# 10. Conditional with input (uncomment to use)
# user_input = input('Enter a number: ')
# if user_input.isdigit():
#     print('You entered a number.')
# else:
#     print('That is not a number.')

# 11. Greatest of three numbers
g1 = 12
g2 = 25
g3 = 7
if g1 >= g2 and g1 >= g3:
    print(f'{g1} is the greatest')  # Executes if g1 is greatest or tied
elif g2 >= g1 and g2 >= g3:
    print(f'{g2} is the greatest')  # Executes if g2 is greatest or tied
else:
    print(f'{g3} is the greatest')  # Executes if g3 is greatest

# 12. Check if a number is positive, negative, or zero
num = -4
if num > 0:
    print('Number is positive')
elif num < 0:
    print('Number is negative')
else:
    print('Number is zero')

# 13. Check if a year is a leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

# 14. Check if a character is a vowel or consonant
char = 'e'
if char.lower() in 'aeiou':
    print(f'{char} is a vowel')
else:
    print(f'{char} is a consonant')



# if condition:
#     statement 1

a=5
if a==9:
    print('a is 10')


if a>5:
    print("a is greater than 5")
else:
    print("a is less than 5 or equal to 5")

a=6
if a>6:
    print("a greater than 6")
elif a>5:
    print("a greater than 5")
else:
    print("a is some number")


# greatest of three numbers
a=10
b=20
c=30

if a>=b and a>=c:
    print("a is greatest")
elif b>=a and b>=c:
    print("b is greatest")
else:
    print("c is greatest")

if a>=b:
    if a>=c:
        print("a is greater")
    else:
        print("c is greater")
elif b>=a:
    if b>=c:
        print("b is greater")
    else:
        print("c is greater")

# ternary condition
a=10
x="even" if a%2==0 else "odd"
x

a=18

y="Eligible" if a>18 else "Not Eligible"
y
list_1=["banana","apple","orange"]
list_2=["grape","melon","kiwi","banana"]
fruit="banana"

if fruit in list_1 and fruit in list_2:
    print("fruit in list1 and 2")
else:
    print("fruit not in list")


print("fruit in list1 and 2" if fruit in list_1 and fruit in list_2 else "fruit not in list")

name="Alice"
if "a" in name.lower() or "e" in name.lower or "i" in name.lower() or "o" in name.lower() or "u" in name.lower(): 
    print("name contains a vowel")
else:
    print("name does not contain a vowel")




# check whether a number is positive, negative or zero
# check the year is leap year or not
# get two list, list1=[1,2,3,4,3] and list2=[1,2,3,4]
# on these two list which list has maximum 3 in it



list(range(1,10))

# range 3 parameter
# start, stop, step
# start -> start of index
# stop -> end of index but last number -1
# step -> how many steps to pass default is 1


{0:list(range(11,2,-2))}




class string_1:
    def __init__(self, s: str):
        self.s=s
    def count(self):
        u=l=c=v=sp=0
        for ch in self.s:
            if ch.isupper():
                u+=1
            elif ch.islower():
                l+=1
            if ch.lower() in "aeiou":
                v+=1
            elif ch.isalpha():
                c+=1
            elif ch==" ":
                sp+=1
            print("Uppercase:",u)
            print("Lowercase:",l)
            print("Vowels:",v)
            print("Consonants:",c)
            print("Spaces:",sp)
onj=string_1(input("Enter a string: "))
onj.count()