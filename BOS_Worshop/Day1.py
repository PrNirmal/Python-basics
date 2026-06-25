# "",'',""""""

a="Nirmal"

# '',"",""""""

# anam
"""
Nirmal Is a programmer
"""

name="Nirmal"
name2='nirmal'
name3="""nirmal"""

# dir(name)
# dir("")
# dir([])

# 'capitalize', 'casefold', 'center', 'count', "encode", 'endswith',
# 'expandtabs', 'find', "format", "format_map", 'index', 'isalnum',
# 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
# 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
# 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
# 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

# capitalize,
# capitalize will make the first letter to uppercase
name2="nirmal"
name2.capitalize()

# casefold
name2="NIRMAL"
name.casefold()

#center
name2="Raj" #3
name2.center(20,)#name2 change to 10 characters ,with the char "o"

name2="Nirmal"
# index:0,1,2,3,4,5
name2[0]
name2[1]
name2[5]
# name2[6] returns out of range error

# count
name2="raja is nirmal's friend"
name2.count("a",0,4)

# endwith

name2="Nirmal is a boy"
# nirmal
# 0,1,2,3,4,5,
name2.endswith("a",0,5)

# expandTabs
name2="Nirmal \tis a boy"
name2.expandtabs(18)
# to expand the size of the tabs

# find
name2 ="Kumar is a boy playing football"

name2.find("o",26)

# format
print("This is an example for format{1},{0},{2}".format(10,20,30))

# index
name2 ="Kumar is a boy playing football"
name2.index("u",4,20)

# index and find -> char index return
# difference index char not found returns value error / returns -1

# 'isalnum',
name2="Nirmal2"
name2.isalnum()

# 'isalpha',
name2="Nirmal "
name2.isalpha()
# 'isascii',
name2="Nirmal!😄"
name2.isascii()

# 'isdecimal',
name2="-10898"
name2.isdecimal()
# this accepts unicode for number

# 'isdigit',
name2="10898"
name2.isdigit()
# it accepts digits only

# 'isidentifier', 'islower',

# join
nam5="Nirmal"
join_name="hello world"
print(nam5.join(join_name))

# ljust
name6="Nirmal"
print(name6.ljust(9,"1"))

#