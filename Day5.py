                                  #Classes in pyhton
"""
Note : Every method in a class should have self as a first parameter so,
      with the self we can get the reference of the current object and can access variables that belongs to the class
     class is a blueprint for creating objects.
     class is a collection of two things ---> Data (attributes) and Methods
    1.All the class should have a  __init__ function which is always executed when the object is been created .
    2.Also called as Constructor takes self as an parameter
    3.We can give any name instead of using self
   
 """

class Employee():
    company_name="Cdac" # class level attribute (can be accessed using class name)
    #Default constructor
    def __init__(self):
        print("Default constructor is called")

   #Parameterized Constructor
    def __init__(self,name,age,group):
        self.name=name
        self.age=age
        self.group=group
    def __str__(self):
        return f"{self.name} ({self.age})"

    def display(self):
        print("Display method is been called")



p1 = Employee("Tushar",23,"HPC-Tech")

print("Name:",p1.name)
print(f"Age: {p1.age}yrs")

print(p1)


p1.display()

print()

######################################################################################################################

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def cal_avg(self):
        sum=0
        for val in self.marks:
            sum +=val
        avg = sum//3
        print("Name:",self.name)
        print(" Average score is:",avg)

s1 = Student("Tushar",[65,88,97])

s1.cal_avg()