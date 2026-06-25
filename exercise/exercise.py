# list_1=[1,2,3,4]
# # 1
# sum=0
# for i in range(len(list_1)):#0
#     sum+=list_1[i]
# print(sum)
#
# # 2
# odd=0
# even=0
# list_1=[1,2,3,4]
# for i in range(len(list_1)):
#     if list_1[i]%2==0:
#         even+=list_1[i]
#     else:
#         odd+=list_1[i]
# differ=even-odd
# print(even)
# print(odd)
# print(differ)
#
# # 3
# list_2=[6,7,8,9]
# list_1=[1,2,3,4]
# # list_3=[7,9,11,13]
# list3=[]
# for i in range(len(list_1)):
#     a=list_1[i]+list_2[i]
#     list3.append(a)
# print(list3)
#
# # 4
# list_2=[6,7,8,9]
# list_1=[1,2,3,4]
# list_3=[7,9,11,13]
# list_4=[]
#
# for i in range(len(list_1)):
#     a=list_2[i]-list_1[i]
#     list_4.append(a+list_3[i])
#
# print(list_4)
#
# # 5
# list_2=[6,7,8,9]
# list_5=[]
# sum=0
# for i in range(len(list_2)):
#     if i not in [1,3]:
#         sum+=list_2[i] #6+8=14
#     else:
#         list_5.append(list_1[i])
# list_5.insert(0,sum)
# print(list_5)
#
# # 6
# st="length"
# st2="bredth"
# newlist=[]
# for i in st:
#     for j in st2:
#         if i==j:
#             newlist.append(i)
#
# print("the repeated letters in the two strings are",end=" ")
#
# for i in range(len(newlist)):
#     if i!=len(newlist)-1:
#         print(newlist[i],end=",")
#     else:
#         print("and "+newlist[i])
#
# # 7
# dict1={"name":"nirmal","age":59}
# dict2={"name":"ravi","age":18}
#
# # if i want to swap the age of dict1 and dict2
# dict2["age"],dict2["age"]=dict1["age"],dict2["age"]
#
# check=True
# while(check):
#     rows = int(input("please enter no of rows above 3"))
#
#     # top set
#     for i in range(rows):
#         for j in range(rows-i-1):
#             print(" ",end="")
#         for k in range(i+3):
#             print("* ",end="")
#         print()
#     l=k+1
#     # second set
#
#     for i in range(rows-1):
#         for j in range(i+1):
#             print(" ",end="")
#         for k in range(l-i-1):
#             print("* ",end="")
#         print()
#     value=input("Do you want to continue y/n")
#     if(value=="y"):
#         continue
#     else:
#         check=False
#
# # factorial:
#
# def value(num):
#     if num==1:
#         return 1
#     else:
#         return num*value(num-1)
#
#
# print(value(5))
#
# balls=['green'] * 5
#
# l1=[1,2,6]
# l2=[3,4,5]
# l3=[]
# for i in [l1,l2]:
#     for j in i:
#         l3.append(j)
# print(l3)
# list_new=[j for i in [l1,l2] for j in i]
# print(list_new)
#
#
# def is_valid(arrangement):
#     """Check if the arrangement has no two adjacent balls of the same color."""
#     for i in range(1, len(arrangement)):
#         if arrangement[i] == arrangement[i - 1]:
#             return False
#     return True
#
#
# def backtrack(remaining, current, result):
#     """Use backtracking to generate all valid arrangements."""
#     if not remaining:
#         if is_valid(current):
#             result.append(current)
#         return
#
#     for color in remaining:
#         new_remaining = remaining.copy()
#         new_remaining.remove(color)
#         backtrack(new_remaining, current + [color], result)
#
#
# def count_valid_arrangements(colors):
#     """Count the number of valid arrangements."""
#     result = []
#     backtrack(colors, [], result)
#     return len(result)
#
#
# def get_user_input():
#     """Get ball counts from user input."""
#     green_count = int(input("Enter the number of green balls: "))
#     yellow_count = int(input("Enter the number of yellow balls: "))
#     red_count = int(input("Enter the number of red balls: "))
#     return ['green'] * green_count + ['yellow'] * yellow_count + ['red'] * red_count
#
#
# # Get ball counts from user
# balls = get_user_input()
#
# # Get all valid arrangements
# num_valid_arrangements = count_valid_arrangements(balls)
# print(f"The number of valid arrangements is: {num_valid_arrangements}")
#
#
# alen=[]
# for i in range(1,len(alen)):
#     print("hi")
#
# remain=[1,2,3]
# for i in tuple(remain):
#     print(i)

# word = input("Enter the String")
or_word = "Banana"
or_word = or_word.upper()
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
vowels = ['A', 'E', 'I', 'O', 'U']
# match="na"
letter_v = []
letter_c = []
score_0 = 0
score_1 = 0
player1 = input("player_1 for vowels")
player2 = input("player_1 for consonants")
result = {player1: score_0, player2: score_1}
print(player1)
for i in range(len(or_word)):
    if or_word[i] in consonants and or_word[i] not in letter_c:
        letter_c.append(or_word[i])
    elif or_word[i] in vowels and or_word[i] not in letter_v:
        letter_v.append(or_word[i])
print(letter_v, letter_c)

for index in range(2):
    if index == 0:
        letter_chosen = letter_v
    else:
        letter_chosen = letter_c
    sub_add=0
    word=or_word
    for l in letter_chosen:
        initial = word.count(l)
        sub_add +=  initial
        for j in range(initial):
            pos = word.index(l)
            for i in range(pos + 1, len(word)):
                sub_add += 1
                print(word)
            word = word.replace(word[pos], '', 1)
        print(sub_add)
    word=or_word
    if (index == 0):
        # score_0 = sub_add
        result[player1]=sub_add
    else:
        # score_1=sub_add
        result[player2]=sub_add

if (result[player1] > result[player2]):
    print(f'{player1} {result[player1]}')
elif (result[player1] < result[player2]):
    print(f'{player2} {result[player2]}')
else:
    print("Draw")

#         test_word=word
#         for test in range(word.count(l)):
#             match = ''
#             for k in range(test_word.index(l), len(test_word)):
#                 match += test_word[k]
#                 print(match)
#                 sum = 0
#                 for i in range(len(test_word) - len(match) + 1):
#                     x = 0
#                     new = i + len(match)
#                     num = 0
#                     for j in range(i, new):
#                         if (test_word[j] == match[x]):
#                             num += 1
#                             x += 1
#                     if (num == len(match)):
#                         sum += 1
#                 if index == 0:
#                     score_0 += sum
#                 else:
#                     score_1 += sum
#                 remove_w = test_word[:test_word.index(l) + 1]
#                 test_word = test_word.replace(remove_w, '')
#     result[player1] = score_0
#     result[player2] = score_1

# Enter your code here. Read input from STDIN. Print output to STDOUT
string=input()
list_1=list(string)
list_cap=[]
list_odd=[]
list_small=[]
list_even=[]
for i in list_1:
    if i.isupper():
        list_cap.append(i)
    elif i.islower():
        list_small.append(i)
    elif(i.isdigit()):
        if(int(i)%2==0):
            list_even.append(i)
        else:
            list_odd.append(i)
sorted_list=[i for j in [list_small,list_cap,list_odd,list_even] for i in sorted(j)]
print("".join(sorted_list))
