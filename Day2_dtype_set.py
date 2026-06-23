# Data types

# 3. Set

# --> {}
# --> No Changeable 
# --> No Duplicate
# --> N0 Indexing

# a={'nisarg','raj','ronak','kunal','sahil','pratik','deep','jay','raj'}
# print(type(a))
# a.add('Ram')
# a.clear()
# a.pop()
# a.copy()
# a.remove('kunal')
# print(len(a))

# print(a)

# ***********************************************

# 1. Create a set of 5 unique numbers.
numbers ={10,20,30,40,50}
print(numbers)

# 2. Add a new element to a set using add().
numbers ={10,20,30,40,50}
numbers.add(34)
print(numbers)

# 3. Remove an element from a set using remove().
numbers ={10,20,30,40,50,34}
numbers.remove(34)
print(numbers)

# 4. Check if a value exists in a set.
if 50 in numbers:
    print('value exists')
else:
    print('value not existed')

# 5. Create two sets and find their union.
numberss ={10,20,30,40,50}
numberss2={10,22,34,55,60,50}
result=numberss.union(numberss2)
print(result)

# 6. Find the intersection of two sets.
res=numbers.intersection(numberss2)
print(res)

# 7. Create a set and convert it to a list.
numbers ={10,20,30,40,50}
numbers.clear()
print(numbers)

# 9. Find the difference between two sets.
r=numberss2.difference(numberss)
print(r)

# 10. Add multiple elements to a set using update().
numbers ={10,20,30,40,50}
numbers.update([34,35,36,37])
print(numbers)
