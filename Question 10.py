#Question 10

#Write a program which accepts a sequence of comma separated 4 digit binary 
#numbers as its input and then check whether they are divisible by 5 or not. 
#The numbers that are divisible by 5 are to be printed in a comma separated 
#sequence.
#Example:
#0100,0011,1010,1001
#Then the output should be:
#1010
#Notes: Assume the data is input by console.

numbers = input("Enter comma seperated numbers: ")

numbers = numbers.split(",")
numbers = list(map(int, numbers))
divis = []

for i in range(len(numbers)):

    if(int(numbers[i]) % 5 == 0):
        divis.append(numbers[i])

print(divis)