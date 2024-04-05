#List in python is same as ArrayList or Vector in C++ ,
# it basically means growing or dynamic array
#List in python is mutable
#List has following basic methods

"""
append() Adds an item to the end of the list
extend() Adds items of lists and other iterables to the end of the list
insert() Inserts an item at the specified index
remove() Removes item present at the given index
pop()	 Returns and removes item present at the given index
clear()	 Removes all items from the list
index()	 Returns the index of the first matched item
count()	 Returns the count of the specified item in the list
sort()	 Sorts the list in ascending/descending order
reverse() Reverses the item of the list
copy()	 Returns the shallow copy of the list

"""
#Some of the applications of List
# To-Do List
# Dynamic Data Storage


# Creating a list of fruits
fruits = ['apple', 'banana', 'orange', 'pineapple']

# Accessing elements of the list
print("The first fruit is:", fruits[0])  # Output: The first fruit is: apple


# Modifying elements of the list
fruits[1] = 'kiwi'
print("After replacing 'banana' with 'kiwi':", fruits)

# Adding elements to the list using append() function which will add at the end of the list
fruits.append('watermelon')
print("After adding 'watermelon':", fruits)

# Removing elements from the list using pop() function
removed_fruit = fruits.pop(2)
print("Removed fruit:", removed_fruit)  # Output: Removed fruit: orange
print("After removing 'orange':", fruits)

# Looping through the list


print(f"List of Fruits:",fruits)

print()

#2-D List in python

print("2-D Array Traversing")

matrix =[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

for rows in matrix:
    for col in rows:
        print(col,end=" ")
    print()

print()
# Basic Question related to List ---> Remove Duplicate from a List
print("Array of unique elements")
numbers = [10,20,20,30,40,30,50]
uniques =[]

for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)


