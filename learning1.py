x=5
y=7
x

from pythonProject.functions import Print_statement

sample=Print_statement()
sample.printStatement()

from typing import List
# class Solutions:
#     def twosums(self,nums:List[int],target:int)->List[int]:
#         seen={}
#         for i,num in enumerate(nums):
#             complement=target-num
#             if  complement in seen:
#                 return [seen[complement],i]
#             seen[num]=i


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(l1.val)
        print(l2.val)

ch=Solution()
print(ch)
bh=ch
ch.addTwoNumbers([10,20,30],[1,2,3])


# obj1=Solutions()
# obj1.twosums([1,2,3,4,5],9)

# Python program showing
# a scope of object

def some_func():
    print("Inside some_func")
    # var=0
    def some_inner_func():
        global var
        var=10
        print("Inside inner function, value of var:",var)
    some_inner_func()
    print("Try printing var from outer function: ",var)
some_func()