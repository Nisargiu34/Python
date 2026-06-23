# Data types

# 3. Dictionary

# --> {} - pair
# --> No Changeable 
# --> No Duplicate
# --> N0 Indexing

# d = {
#     'name': 'Nisarg',
#     'age': 20,
#     'course':'Python'
#     }

# print(d.get('name'))  
# print(d.get('age'))   
# d.update({'name':'Nishu','city':'Ahmedabad'})    we change value also add new value throught update

# print(d)

# *************************************

# 1. Create a dictionary with 3 key-value pairs and print it.
student={
    'name':'Nisarg',
    'age':20,
    'city':'Ahmedabad'
}
print(student)

# 2. Add a new key-value pair to a dictionary.

student={
    'name':'Nisarg',
    'age':20
}
student['city']='Ahmedabad'
print(student)

# 3. Remove a key from a dictionary using pop().
student ={
    'name':'Nisarg',
    'age':20,
    'city':'Ahmedabad'
}
student.pop('city')
print(student)

# 4. Print all keys of a dictionary.
student ={
    'name':'Nisarg',
    'age':20,
    'city':'Ahmedabad'
}
print(student.keys())

# 5. Print all values of a dictionary.
student ={
    'name':'Nisarg',
    'age':20,
    'city':'Ahmedabad'
}
print(student.values())

# 6. Update the value of an existing key
student ={
    'name':'Nisarg',
    'age':20
}
student['age']=21
print(student)

# 7. Check if a key exists in a dictionary.
if 'age' in student:
    print('value exists')
else:
    print('Value does not exited')
 

# 8. Create a dictionary and print the number of items.
student={
    'name':'Nisarg',
    'age':20,
    'city':'Ahmedabad'
}
print(len(student))

# 9. Create a dictionary and print only the keys.
print(student.keys())

# 10. Merge two dictionaries into one.
Teacher={
    'class':'10th',
    'salary':25000
}

combine=student.copy()
combine.update(Teacher)
print(combine)



