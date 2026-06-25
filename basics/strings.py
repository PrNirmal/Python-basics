# String
# Strings in python are surrounded by either single quotation marks, or double quotation marks

# capitalize
string = "beautifull"
print(string.capitalize())  # will capitalize the first letter of the string

# casefold
string1 = "cat"
print(string1.casefold())  # will convert the string to lowercase

# center
string2 = "nirmal"
print(string2.center(20, "p"))  # used to center the string
print(string2.center(20, " "))
print(string2.center(20, "\n"))

# count
string3 = "there is a box,inside the box is box nothing"
print(string3.count('box'))  # used to find no of times the given argument is present
print(string3.count('i'))
print(string3.count(''))  # it will return the entire lenth of the string

# encode
string4 = "some"
print(string4.encode())  # used to encode the string(i.e in binary)

# endswith
string5 = "code"
print(string5.endswith('e'))  # return true if it ends with the passed letter
print(string5.endswith('c'))  # return false if it not ends with the passed letter
print(string5.endswith(''))  # return true if it ends with the passed letter

# expandtabs
string6 = "w\to\tr\tk"
print(string6.expandtabs(2))  # used to increase the tab size by 2 spaces(2 space were passed to the tab)
print(string6.expandtabs(4))  # uesd to increase the tab size by 4 spaces(4 space were passed to the tab)
print(string6.expandtabs(6))  # uesd to increase the tab size by 6 spaces(6 space were passed to the tab)
print(string6.expandtabs(8))  # uesd to increase the tab size by 8 spaces(8 space were passed to the tab)
print(string6.expandtabs())  # default the size will be 8
print(string6.expandtabs(9))  # uesd to increase the tab size by 2 spaces(9 space were passed to the tab)
# the no passed is no of spaces

# find
string7 = "thisisthepython"
string8 = "this is the python"
print(string7.find('python'))  # this will return the staring letter index value
print(string8.find('thep'))  # if the value no in the string then return -1
print(string8.find(' '))
print(string7.find('this'))
print(string7.find())  # if no value passed,then ends with error
print(string7.find(''))  # return 0 first position
print(string8.find('the', 5,
                   14))  # we can also mention the start and end point to get faster by,default start is 0,end is end of string

# format
string8 = "my name is {}"
print(string8.format('nirmal'))  # used to format (i.e)to pass the value in the place{}
print(string8.format('nirmal'))  # nothing will be passed
string8 = "My name is {fname}, I'm {age}".format(fname="nirmal", age=19)
print(string8)
string8 = "My age is {1} and I'm {0}".format("nirmal",
                                             19)  # can also be used by index to place in a particular position
print(string8)
string8 = "My name is {}, I'm {}".format("nirmal", 19)
print(string8)
x = "nirmal"
string8 = "My name is {x}".format(x=x)
print(string8)

# another method
string8 = f"hi,my name is {x}"
print(string8)

# format_map
x = {'a': 'nirmal', 'b': "19"}
string_8 = "My name is {a},I'm {b}".format_map(x)  # used to return a dictionary key’s value
print(string_8)
string_8 = "{a},{b}".format_map(x)
print(string_8)
profession = {'name': ['nirmal', 'ajay'], 'profession': ['Engineer', 'Mba'], 'age': [22, 19]}
string_8 = '{name[0]} is an {profession[0]} and he is {age[1]} years old.'.format_map(profession)
print(string_8)
string_8 = '{name[1]} is an {profession[1]} and he is {age[0]} years old.'.format_map(profession)
print(string_8)

# index
string9 = "this is program"
print(string9.index('program'))  # it will return the index of the word present
print(string9.index(''))  # if nothing is passed it will return 0

# isalnum
string10 = 'abc45gf'  # return true if the value is albhabet or number else false(i.e)special character like!,#,$
print(string10.isalnum())
string10 = 'abc45gf#'
print(string10.isalnum())
string10 = 'abc'
print(string10.isalnum())

# isalpha
string11 = 'abcd'  # return true is the value in the string is alphabet else false
print(string11.isalpha())
string11 = 'abc1x'  # return false
print(string11.isalpha())

# isascii
string12 = '2s%&$'  # return true if the value is non ascii
print(string12.isascii())
string12 = 'ñ'  # return false as it is non ascii #unicode-for emoji and text
print(string12.isascii())
string12 = '±'  # return false as it is non ascii #unicode-for emoji and text
print(string12.isascii())

# isdecimal
string13 = '30'  # The isdecimal() method returns True if all the characters are decimals (0-9).
# This method is used on unicode objects
print(string13.isdecimal())
string13 = '\u0030'  # unicode for 3
print(string13.isdecimal())
string13 = '\u0047'  # unicode for G
print(string13.isdecimal())

# isdigit
string14 = '67'  # method returns True if all the characters are digits, otherwise False.
# Exponents, like ², are also considered to be a digit.
print(string14.isdigit())
string14 = '\u00B2'  # unicode for ²
print(string14.isdigit())
    
# isidentifer
string15 = '2sa'  # returs false beause it starts with integer
print(string15.isidentifier())
string16 = '_sa'  # returs true, its obey python rules for creating an identifier
print(string16.isidentifier())
string17 = 'satya1'  # returs true
print(string17.isidentifier())
string18 = 'sa@'  # returs false beause it has special character
print(string18.isidentifier())

# islower
string16 = 'code'
print(string16.islower())  # return true if the string is lower else false
string16 = 'codE'
print(string16.islower())  # return true if the string is lower else false

# isnumeric
string17 = '23'  # return true if the string is numeric else false
print(string17.isnumeric())
string17 = '23a'
print(string17.isnumeric())

# isprintable
string18 = 'abc\nefg'  # returns true if it doesnt contain any tags
print(string18.isprintable())
string18 = 'abcefg'
print(string18.isprintable())

# isspace
string19 = ' '
print(string19.isspace())
string19 = '\t'
print(string19.isspace())
string19 = '\n'
print(string19.isspace())
string19 = ' the nirmal'  # chexck whether the string is space if not return false
print(string19.isspace())

# istitle
string20 = 'Tom'
print(string20.istitle())  # return true if the starting letter in uppercase else false
string20 = 'tom'
print(string20.istitle())

# isupper
string21 = 'TOM'  # check whether the string in uppercase return true if it is in uppercase else false
print(string21.isupper())

# join
txt = ('hello', 'world')  # used to join elements of the sequence separated by a string separator
print(" ".join(txt))
txt = ["the","|", "man"]
print(" | ".join(txt))
txt = "nirmal"
print(" ".join(txt))
txt = {'1', '3', '5', '5'}
print("-#-".join(txt))  # as set doesn't contain duplicate elements so 5 is removed
dic = {'Geek': 1, 'For': 2, 'Geeks': 3}
string = '_'.join(dic)  # join the keys
print(string)

# ljust(left justify)
string41 = 'hi'
print(string41.ljust(10, 'm'))  # it will make the length of the string as 10 with m(from the end)
print(string41.ljust(10), string41)  # by default it is white space
print(string41.ljust(20, "o"))

# lower
string30 = 'CAT'  # used to covert the string to lower case
print(string30.lower())

# lstrip
string35 = '    hi      '
x = string35.lstrip()  # used to remove white spaces to the left of the string
print('hello', x, 'welcome')
string35 = 'hi       '
x = string35.lstrip("noth")  # as h is in the string h will be removed
print(x)


string35 = 'nothhi       '
x = string35.lstrip()  # as first noth will be removed then hi will be there as in noth h is present so h will be removed
print(x)  # and the result will be i

# maketrans
# maketrans()function is used to construct the transition table
# i.e specify the list of characters that need to be replaced in the whole string or the characters that need to be deleted from the string
# Syntax : maketrans(str1, str2, str3)
# Parameters :
# str1 : Specifies the list of characters that need to be replaced.
# str2 : Specifies the list of characters with which the characters need to be replaced.
# str3 : Specifies the list of characters that needs to be deleted.
# Returns the translation table which specifies the conversions that can be used by translate()

# translate
# To translate the characters in the string translate() is used to make the translations
# Syntax : translate(table, delstr)
# Parameters :
# table : Translate mapping specified to perform translations.
# delstr : The delete string can be specified as optional argument is not mentioned in table.
# Returns : Returns the argument string after performing the translations using the translation table.

main_str = "weeksyourweeks"
str_1 = "wy"  # the changing argument should be in same length
# str_2="he is"
str_2 = "gf"
# str_3 = "u"


table = main_str.maketrans(str_1, str_2)  # it return ascii
print(table)

main_str.translate({119:101})
# the_table = {119: 103, 121: 102, 117: None}
print("The string before translating is : ", end="")
print(main_str)
print("The string after translating is : ", end="")
print(main_str.translate(table))

# partition
string39 = 'python is a interpreted programming language'  # it will return in tuple format
print(string39.partition('interpreted'))
string39 = 'python is a interpreted programming language'
print(string39.partition(' '))
string39 = 'python is a interpreted programming language'
print(string39.partition('is'))

# removeprefix
string28 = 'garbage'

print(string28.removeprefix('ga'))  # used to remove the prefix
string28 = 'garbage'
print(string28.removeprefix(
    'ba'))  # if the passed string is not as prefix then it will return the same string without removing

# removesuffix
string29 = 'garbage'
print(string29.removesuffix('ge'))  # used to remove the suffix
string29 = 'garbage'
print(string29.removesuffix(
    'be'))  # if the passed string is not as suffix then it will return the same string without removing

# replace
string24 = 'my bag'
print(string24.replace('bag', 'book'))  # used to replace the string with another string
string24 = 'my bag'
print(string24.replace(' ', '_'))

# rfind
string25 = "i'm nirmal and i'm 19"
print(string25.rfind('i'))  # The rfind() method finds the last occurrence of the specified value.
string25 = 'where is he'  # The rfind() method returns -1 if the value is not found.
print(string25.rfind('why'))
string25 = 'where is he where'
print(string25.rfind('where'))
string25 = 'where is he where'
print(string25.rfind('where', 0,
                     9))  # we can also mention the start and end point to get faster by,default start is 0,end is end of string

# rindex
string26 = 'where it is it'
print(string26.rindex('it'))  # same as rfind
string26 = 'where it is it'
print(string26.rindex('it', 0, 12))

# rjust(right justify)
string42 = 'hi'  # it will make the length of the string as 10 with m(from the beginning)
print(string42.rjust(10, 'n'))
print(string42.rjust(10))  # default white space

# rpartition(right partition)
string40 = 'python is a interpreted programming is language'  # it starts partition from right
print(string40.rpartition('is'))

# rsplit(split from right)
string37 = 'hello world'  # return in list format
print(string37.rsplit())  # default split by white space
string37 = 'hello me its me fello'  # return in list format
print(string37.rsplit('me'))  # default split by white space#me will not be considered the list will like before me
# and after me

# rstrip
string34 = '    hi      '
x = string34.rstrip()  # it will remove white spaces at the end
print('hello', x, 'welcome')
string34 = 'd   hi  l    d'
print(string34.rstrip('d'))

# split
string36 = 'hello world'  # split from left
print(string36.split())
string36 = 'hello world welcome'  # split from left
print(string36.split('world'))
string36 = 'hello world welcome hello world welcome'  # split from left
print(string36.split('world'))  # the result will be in list

# strip
string32 = '    hi      '  # remove white space
x = string32.strip()
# print(string32)
print('hello', x, 'welcome')
# strip2
string33 = 'wwwwwhiwwwww'
print(string33.strip('w'))

# splitness
string38 = 'he is reading\nhe is writing'  # it will return in list
print(string38.splitlines())  # the string before the line and after the line

# startswith
string27 = 'rat'
print(string27.startswith('r'))  # return true if it starts with the passed string else false
string27 = 'Rat'
print(string27.startswith('r'))
print(string27.startswith(''))  # return true if nothing is passed

# swapcase
string31 = 'italy'
print(string31.swapcase())
string31 = 'itAly'
print(string31.swapcase())

# title
string23 = 'banana'
print(string23.title())  # will change the first letter of the string to uppercase

# traslate
make_t = "Hello Sam"
table = {97: 80}  # convert s-83 as p-80(ascii code)
make_t.translate(table)

# upper
string22 = 'apple'
print(string22.upper())  # convert the string to uppercase
string22 = 'apPle'
print(string22.upper())

# zfill
string43 = 'hi'  # Fill the string with zeros until it is 10 characters long
print(string43.zfill(10))
print(string43.zfill(20))

import random
import time
while(True):
    print("Searching \nAnalyzing'Estimating Approximate Location of \n'Compressing\n'Downloading")
    for i in range(10):
        for j in range(10):
            print(random.random(),end="")
    print()

n=[1,2,3]
n.remove(1)

name="niRmal"
result=""

for i in name:
    if(i.islower() and i.isalpha()):
        result+=i.upper()
    elif(i.isupper() and i.isalpha()):
        result+=i.lower()
    else:
        continue
print(result)

