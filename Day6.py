                                      #Static Method
""" Static Methods are those methods which do not use self parameter and works at class level
    Does not required self as parameter"""
class Demo:
   """ decorator --> allows us to wrap another function to extend the behaviour of the wrapped function,
   without actually modifying it.
   in short takes a method and chnages its behaviour and return a method
"""
   @staticmethod  # decorator
   def cllg_name():
        print("IET Pune")

Demo.cllg_name()


########################################################################################################################

class Account:

    def __init__(self,bal,acc_no):
        self.bal = bal
        self.acc_no = acc_no
    def credit(self,amount):
        self.bal += amount
        print("Rs.",amount,"is credited in your account")


    def debit(self,amount):
        self.bal -= amount
        print("Rs.", amount, "is debited from your account")


    def get_balance(self):
        print("Current Balance is:", self.bal)

acc1 = Account(10000,"2713645908488")

acc1.debit(4500)
acc1.get_balance()

print("----------------------------------------------------------------------------------------------------------------")

#Private Data memebers and Methods

#Note: For defining a member or method as private we need to define it with "__" (double underscore)

class Person:
    __name = "Tushar"
    def __salary(self):
        print("The salary is: 90000")
    def details(self):
        self.__salary()
        print("Name is: ",self.__name)

p1 = Person()

p1.details()

print("----------------------------------------------------------------------------------------------------------------")

#Inheritence

#Single level Inheritence
print("Single level Inheritence")
class Car:
    clutch = False
    acc = False
    brk = False
    @staticmethod
    def start(self):
        Car.acc = True;
    def stop(self):
        Car.brk = True;

class Toyota(Car):
    def start(self):
        self.clutch = True
        print("Car has started.....")

    def stop(self):
        print("Car has stopped!!")

car1 = Toyota()

car1.start()

car1.stop()

#Multilevel Inheritence
print()
print("Multilevel Inheritence")
class Fortuner(Toyota):

    colour = ""

    def show_color(self):
        self.colour = "black"
        print("colour is:",self.colour)

car2 = Fortuner()

car2.show_color()
car2.start()
car2.stop()


#Multilevel Inheritence
print()
print("Multiple Inheritence")

class A:
    var_a = "variable of class A"
class B:
    var_b = "variable of class B"
class C(A,B):
    var_c = "variable of class C"


c1 = C()

print(c1.var_a)
print(c1.var_b)
print(c1.var_c)
