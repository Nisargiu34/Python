# Data types

# 1. List

# --> []
# --> Changeable 
# --> Allow Duplicate
# --> Indexing

# a1 =['nisarg','raj','ronak','kunal','sahil','pratik','deep','jay','raj']
# # a=['nishu','kana']

# # print(type(a)) 

# # a1.append('dipak')  For adding values
# # a1.sort()          For acsending order
# # a1.reverse()       For deseding order'
# # a1.extend(a)       For add another list 
# # a1.insert(1,'dev') For add value with defined index
# # a1.remove('deep')  For remove perticular list value
# # a1.clear()         For delete all the values
# # a1.copy()            For copy list
# # print(a1.count('raj'))  for finding duplicate values again
# # a1.pop()           #  for removing last vlaue
# # a2=a1.index('kunal')   for counting index number

# print(a1)

# 1. Create a list of 5 colors and print it.

colour = ['red','yellow','pink','black','white']
print(colour)

# 2. Add a new item to a list using append().
colour.append('purple')
print(colour)

# 3. Remove an item from a list using remove().
colour.remove('yellow')
print(colour)

#4. Find the length of a list using len().
print(len(colour))

# 5. Print the first and last element of a list.
print(colour[0])
print(colour[3])

# 6. Replace the third element in a list with a new value.
colour[2]='blue'
print(colour)

# 7. Sort a list of numbers.
colour.sort()
print(colour)

# 8. Count how many times a value appears in a list.
colour.append('red')
print(colour.count('red'))

# 9. Create a list of 5 numbers and print the maximum number.
num = [20,30,40,50,34]
print(max(num))

# 10. Reverse a list without using slicing.
num.reverse()
print(num)