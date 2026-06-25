# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed

set1={'a','b','c','d'}
set2={'d','e','f','g'}
# set3=set1.union(set2)
set3=set1.intersection(set2)
set3=set1.symmetric_difference(set2)
print(set3)
dir(set1)
# 'add', 'clear', 'copy', 'difference', 'difference_update','discard', 'intersection',
#  'intersection_update', 'isdisjoint', 'issubset', 'issuperset','pop', 'remove',

# add
set1.add('s')
print(set1)

set4={'a'}
set4.add('b')
set4.add('c')
print(set4)