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

