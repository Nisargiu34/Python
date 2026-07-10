# 1. Take name(str),age(init), height(float),and is_student(bool) as input. Use if-else to determine whether the person is an adult or minor.

# name = input('Enter Name : ')
# age = int(input('Enter age : '))
# height= float(input('Enter height: '))
# is_student=input('Are you student? (True/False):') == 'True'
# if age>=18:
#     print('Adult')
# else:
#     print('Minor')
    


# 2. Take 5 numbers from user and store them in list. Separate them into even numbers of list and odd numbers of list.
# total=[]

# n1=int(input('Enter first num :'))
# n2=int(input('Enter second num :'))
# n3=int(input('Enter third num :'))
# n4=int(input('Enter fourth num :'))
# n5=int(input('Enter fifth num :'))

# print(n1)
# print(n2)
# print(n3)
# print(n4)
# print(n5)

# print(type(n1))
# total.append(n1)
# print(total)

# total.append(n2)
# print(total)

# total.append(n3)
# print(total)

# total.append(n4)
# print(total)

# total.append(n5)
# print(total)

# if n1%2 ==0:
#     print('even')
# else:
#     print('odd')
    
# if n2%2==0:
#     print("even")
# else:
#     print("odd")
    
# if n3%2==0:
#     print("even")
# else:
#     print("odd")
    
# if n4%2==0:
#     print("even")
# else:
#     print("odd")
    
# if n5%2==0:
#     print("even")
# else:
#     print("odd")
    

# 3.store 5 subject marks in tuple.Calculate average and print pass if average>50 , otherwise fail.

# maths=98
# science=78
# gujarati=100
# hindi=75
# Computer=85

# a=()
# print(type(a))

# a=(maths+science+gujarati+hindi+Computer)
# print("type of a ")
# print(type(a))
# print(a)

# avg=a/5
# print(avg)
# print("avg type ")
# print(type(avg))

# if avg>50 :
#     print("Pass")
# else:
#     print("Fail")
    
# 4. Take a single character(str) as input.Check whether it is a vowel, consonant,or digit.

# four=input("Enter a character")

# print("four",type(four))
# print(four)

# digit= int
# print("digit",type(digit))
# vowel = ('a','e','i','o','u','A','E','I','O','U')
# digit=('0','1','2','3','4','5','6','7','8','9')
# print("vowel",type(vowel))
# print("digit",type(digit))

# vowelN=str(vowel)
# print(type(vowelN))
# print(vowelN)

# if four in digit:
#     print("this is digit")
# elif four in vowelN:
#     print("it is vowel")
# else:
#     print("this is consonant")


# 5. Take 10 numbers in a list and convert the list to a set to remove duplicates. print the unique numbers.

Nlist=[11,20,30,11,20,30,55,44,99,34]
print("Nlist class:",type(Nlist))
print(Nlist)

Nset=set(Nlist)
print("Nset Class:",type(Nset))
print(Nset)


# 6.Create a list of 5 floats representing prices .print the highest price using if-else(not max()).

f1=15.25
f2=30.20
f3=90.12
f4=1001.50
f5=500.82

if f1>f2:
    print("F1 bigger then f2")
else :
    print("f2 is bigger then f1")
if f3>f4:
    print("f3 is bigger then f4")
else:
    print("f4 is bigger then f3")
if f5>f1:
    print("f5 is bigger then f1")
else:
    print("F1 is bigger then f5")






