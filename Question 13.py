#Question 13

#Write a program that accepts a sentence and calculate the number of letters 
#and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3

sentence = input("Enter your sentence: ")
letters = 0
digits = 0

for i in range(len(sentence)):
    j = sentence[i]
    if(j.isnumeric()):
        digits += 1
    elif(j.isalpha()):
        letters += 1
    
print(letters)
print(digits)
    