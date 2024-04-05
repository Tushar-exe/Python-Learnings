#Tuples in python is same as List but tuples are immutable

#applications of tuples

#Person Information
#Coordinates



# NOTE : "None" is an object which represents absence of an value

coordinates = (10,20,30)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

print(f"X:{x} Y:{y} Z:{z}")

#unpacking in python

#Unpacking in Python refers to the process of extracting individual elements from a collection, such as a list, tuple, or dictionary,

a , b ,c = coordinates

print(f"A:{a} ,B:{b} ,C:{c}")

my_tuple = (1,2,3,4)

print(my_tuple)

print(my_tuple[2])

#Slicing Tuples

print(my_tuple[1:3])

#Tuple Methods
print(len(my_tuple))

print(my_tuple.count(3))

print(my_tuple.index(3))

#-----------------------------------------------------------------------------------------------------------------------

#Dictionary In Python

"""In Python, a dictionary is a mutable and unordered collection of key-value pairs. 
Each key-value pair in a dictionary is separated by a colon : and the pairs are separated by commas."""

customer ={
    "name" : "Tushar",
    "email" : "tushar@gmail.com",
    "number" : "132457687980",
    "desgination" : "Project Engineer"
}

print(customer.get("name"))

print(customer)

print(customer.values())

phone= input("Enter your Number")

digits_mapping ={
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero"
}

output = ""

for ch in phone:
    output +=digits_mapping.get(ch," ")+" "

print(output)

# Functions in python

#Note : By default all function in python return None
def greet_user(name):
     print(f"Hi {name}")
     print("welcome to CDAC")

greet_user("Tushar")


def square(num):
    return num*num
result = square(3)

print(result)

#Try And Except

try:
    age = int(input("Enter your age"))
    print(f"Entered Age: {age}yrs")
except ValueError:
    print("Invalid input number expected")





