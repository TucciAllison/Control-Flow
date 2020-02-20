
#Programmer: Allison Tucci
#Date: 12/16/2019
#Program: Guess My Number


myNumber = 7

print("\nGuess a number between one and ten\n")

# Ask users to guess
guess = int(input("Enter a Guess: "))

# Keep asking users to guess my number until
# it is equal to my number

while guess != myNumber:
    print("\nNope, guess again: ")
    guess = int(input("Enter a Guess: "))

print("\nCongratulations, you guessed my number!\n")

"""
Programmer: Allison Tucci
Date: 1.23.2020
Program: While Loop nested inside of a For Loop
"""


for i in range(4):
    print("\n")
    print("For Loop " + str(i))
    x = i
    while x >= 0:
        print("\t While Loop: " + str(x))
        x = x - 1


#Programmer: Allison Tucci
#Date: 12/19/2019
#Program: One Through Ten

x = 1

# While loop will see if a condition has been met
# If not it will run again until the condition
# has been met

while x <= 10:
    print(x)
    x += 1


#Programmer: Allison Tucci
#Date 1.6.20
#Program: Running Total, Part II

#This program asks users for five numbers
#It then sums up the numbers

sum = 0

how_many_numbers = int(input("\nHow many numbers would you like to sum up: "))
print("")
for i in range(how_many_numbers):
    enter_a_number = int(input("Enter a number: "))
    sum = sum + enter_a_number

print("\nSum of your numbers is: " + str(sum))


#Programmer: Allison Tucci
#Date 1.7.20
#Program: Average Test Scores
#This program asks users how many tests they wish to average


total = 0
how_many_tests = int(input("\nHow many tests would you like to average: "))
print("")

for i in range(how_many_tests):
    enter_a_score = float(input("Enter a score: "))
    total = total + enter_a_score

average = total / how_many_tests

print("\nAverage Test Score: " + str(round(average, 2)))


#Programmer: Allison Tucci
#Date:1.20.20
#Program: Double For Loop
for i in range(3):
    print("Outer For Loop " + str(i))
    for k in range(4):
        print("\tInner For Loop " + str(k))

print("\n********************\n")

# Programmer: Allison Tucci
# Date: 2.3.2020

#Declare Global Variables Here
name = input("\nWhat is your name? ")
x = 15

#Create Functions Here

# Greeting Function
def greeting():
    print("Hi there " + name + "!")
    print("Very nice to meet you " + name)

#Functions and Local Variable x
def printSomething():
    x = 3
    print(x)

#Functions and Parameters
def printNumber(age): #Function name = printNumber with a PARAMETER of age
    print(age)

#Default Parameter Values
def printTwoNumbers(x,y= 71):
    print("First Parameter(number): " + str(x))
    print("Second Parameter(number): " + str(y))

# Print Sum
def printSum(x,y):
    print(x + y)

#Print Multiple Times
def printMultipleTimes(string, times):
    for i in range(times):
        print(string)

#Call Functions Here

print("\n ****Greetings Function****\n")
greeting()

print("\n ****Print Something Function****\n")
printSomething()

print("\n ****Print Number Function****\n")
printNumber(28)
printNumber(38)

print("\n****Print Two Number Function****\n")
printTwoNumbers(23,78)

print("\n ****Default Parameter Values Function****\n")
printSum(36,29)

print("\n ****Print Multiple Times****\n")
printMultipleTimes("I love computer science", 13)

