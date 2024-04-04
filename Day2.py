#Loops in Python
i = 1
while i <= 5:
    print('*'*i)
    i = i+1

print()
#----------------------------------------------------#

#Number Guessing Game
print("-----Number Guessing Game------")


magic_number = 7
guess_count = 0
guess_limit = 3
print(f"Guess_Count:{guess_count}  Guess_Limit:3")

while guess_count < guess_limit:
    guess = int(input("Make a guess: "))
    guess_count += 1
    guess_remain = guess_limit-guess_count
    print("Remaining guesses are: ", guess_remain)
    if guess_remain == 0 and guess != magic_number:
        print("You Loose the Game!!")
    else:
        if guess == magic_number:
         print("You won!!")
         break

print()

#Car Simulation Game

print("Car Simulation Game")
command=""
started=False
stopped=False


i=1
while i<=4:
    print("Option Menu:")
    print("""    1.start
    2.stop
    3.help
    4.quit
    """)
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
            i = i+1
        else:
            started=True
            print("Car started ready to go...")
            i = i + 1
    elif command == "stop":
        if stopped:
            print("Car stopped already...")
            i = i + 1
        else:
            stopped=True
            print("Car Stopped....")
            i = i + 1
    elif command == "help":
        print("""
        start - to start the car
        stop  - to stop the car
        quit  - to quit the car
        """)
        i = i + 1
    elif command == "quit":
        i = i + 1
        break
    else:
        i = i + 1
        print("Sorry i don't understand that...")
#--------------------------------------------------------------------------------#

#Sum of List

n=int(input("Enter the size of the array: "))
print("Enter Array Elements")
arr=[]

for i in range(n):
    element=int(input())
    arr.append(element)
    #arr.sort()

print(f"The array is: {arr}")
print(f"The sum of elements of the array is: ",{sum(arr)})

#--------------------------------------------------------------------------------#

arr1=[1,1,1,5]

for i in arr1:
    output= ''
    for j in range(i):
        output += 'X'
    print(output)

#--------------------------------------------------------------------------------#

list1=[22,45,68,44,10]
res=0;
large=list1[0]

for num in list1:
    if num>large:
     large=num
     res=large

print("The largest number is", res)