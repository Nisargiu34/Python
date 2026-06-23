# Data types

# 2. Tuple

# --> ()
# --> No Changeable 
# --> Allow Duplicate
# --> Indexing

# a=('nisarg','raj','ronak','kunal','sahil','pratik','deep','jay','raj')
# print(type(a))
# a2=a.count('raj')   counts how many raj name appered
# a2=a.index('jay')   it shows on which index has 'jay'
# print(a2)
# print(len(a))

# print(a)

# *****************************

# 1. Create a tuple of 5 fruits and print it.
fruits=('banana','apple','orange','mango','grapes')
print(fruits)

# 2. Print the second and fourth element of a tuple.
fruits =('apple', 'banana', 'mango', 'orange', 'grapes')
print(fruits[1])
print(fruits[3])

# 3. Find the length of a tuple.
fruits =('apple', 'banana', 'mango', 'orange', 'grapes')
print(len(fruits))

# 4. Check if a value exists in a tuple.
fruits =('apple', 'banana', 'mango', 'orange', 'grapes')
if 'mango' in fruits:
    print('found')
else:
    print('not found')
    

# 5. Convert a tuple into a list.
f_list=list(fruits)
print(f_list)

# 6. Convert a list into a tuple.
f_list=tuple(fruits)
print(f_list)

# 7. Find the index of an element in a tuple.
fruits =('apple', 'banana', 'mango', 'orange')
print(fruits.index('mango'))

# 8. Count how many times a value appears in a tuple.
numbers =(10,20,10,30,10,40,10,10)
print(numbers.count(10))

# 9. Join two tuples together.
tuple1 =(1,2,3)
tuple2 =(4,5,6)
result =tuple1+tuple2
print(result)

# 10. Print the last element of a tuple using negative indexing.
fruits = ("apple", "banana", "mango", "orange", "grapes")
print(fruits[-1])


