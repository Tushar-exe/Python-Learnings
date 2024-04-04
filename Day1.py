
# Basic Of Python Programming

print("Hello World My name is Tushar learning Python")

is_checked= True;
print(is_checked)

# #Checking the type of variable
# print(type(is_checked))
#
# #Taking response from user using input() function
#
# response=input("Welcome to Cdac What is Your Name: ")
# desg =input("Your Designation: ")
#
# print("Hello "+response +" "+desg)
#
# String Demo
#
# birth_year=input("Enter your birth year:")
#
# age=2024-int(birth_year)
#
# print("Your Age in yrs is:",age)
#
# Formatted String In Python
#
# str1="Tushar"
# str2="Patle"
# str= f' {str1} [{str2}] is a coder'

# print(str)

# str3 ="National Super Computing Miss";

# str4=str3.replace("Miss","Mission");

# print(str4)

# print(str3)

# print("National" in str3)

#Arithematic Operator
x=3
x=x+1;
print(x)

is_hot=False;
is_cold=True


#Conditional Statements
if is_hot:
    print("It is a hot day")
    print("Drink Lot of water!!")
elif is_cold:
    print("It is a cold Day")
    print("Wear Warm clothes !!")
else:
    print("It is a lovely Day")

#Logical Statement Example

is_good_credit=True
is_criminal=False

if is_good_credit and not is_criminal:
    print("Person is Eligible for Loan")
else:
    print("Person is not Eligible for Loan")

#Relational Operators
name="Tushar"
length=len(name)

if(length)<3:
    print("Name is too small   ")
elif(length)>50:
    print("Name cannot be greater tha 50 character")
else:
    print("EveryThing looks Good")

#Making some user specific programs

response=int(input("Enter your weight"))
choice=input('(K) for kg or (G) for grams')
ans=0;
if choice.upper() == 'K':
    ans=response
    print(f'you are {ans} kg')
else:
    ans=response*1000
    print(f'you are {ans} grams')

import math
x=3.4
print(math.floor(x))


age=18

if age>=18:
    print("Person is eligible for Vote")
else:
    print("Person is not eligible for Vote")

