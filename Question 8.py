#Question 8

#Write a program that accepts a comma separated sequence of words as input and 
#prints the words in a comma-separated sequence after sorting them 
#alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world

string = input("Enter you comma seperated list of strings: ")

a = (string.split(", "))

for i in range(len(a)):
   
    for j in range(0,len(a)-i-1):
        if(a[j] > a[j+1]):
            a[j], a[j+1] = a[j+1], a[j] #swap places
 
print(a)