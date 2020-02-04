
# Programmer: Allison Tucci
# Date: 2.3.2020

#Declare Global Variables Here
# name = input("\nWhat is your name? ")
x = 15

#Create Functions Here

# Greeting Function
def greeting():
    print("Hi there " + name + "!")
    print("Very nice to meet you " + name)
    print(x)

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
# greeting()
# printSomething()
# print(x)
#printNumber(28)
#printNumber(38)
#printTwoNumbers(23,78)
#printTwoNumbers(45)
#printSum(36,29)
printMultipleTimes("I love computer science", 13)