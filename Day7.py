# Decorator in python

""" Decorator is function which takes a function as a argument and returns a function
    @function_name is used to specify a decorator to be applied on another function"""


def decorator(func):
    def wrapper():
        print("function before enhancing")
        func()
        print("function after enhancing")
    return wrapper


def num():
    print("We will use this function")
    print("and we will enhance this inside a decorator")

called_fun = decorator(num)

called_fun()


print("---------------------------------------------------------------------------------------------------------------")

def decorator(num):
    def wrapper():
        a = num()
        print("Output :",a)
        add = a +5
        return add
    return wrapper

@decorator
def num():
    return 10

result=num()

print("Decorated output :",result)

print("---------------------------------------------------------------------------------------------------------------")

class Person:
    name = "Tushar"
    @classmethod
    def change_Name(cls,name):
        cls.name = name
        print("Changed Name:",name)

p1 = Person()
print("Name :",p1.name)
p1.change_Name("Tushar Patle")