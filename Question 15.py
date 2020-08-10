#Question 15

#Write a program that computes the value of a+aa+aaa+aaaa with a given digit 
#as the value of a.
#Suppose the following input is supplied to the program:
#9
#Then, the output should be:
#11106

val = input('Enter number: ')
val = int(val)

out = val + 11 * val + 111 * val + 1111 * val

print(out)