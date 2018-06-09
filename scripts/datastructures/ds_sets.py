#set data types
set_A={1,2,3,4,5,6,7,8,21}
set_B={1,2,3,4,10}

#And or interesection operation
print(set_A&set_B)

#Or or Union operation
print(set_A | set_B)

print(dir(set_A))
#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint','issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

set_A.pop()
print(set_A)

set_A.remove(2)

#set_A - set_B
print(set_A.difference(set_B))


