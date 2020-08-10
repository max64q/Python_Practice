#Question 11

#Write a program, which will find all such numbers between 1000 and 3000 
#(both included) such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a 
#single line.

start = 1000 
end = 3000

evens = []

for i in range(start, end+1):
    if(i % 2 == 0):
        if(int(i / 10) % 2 == 0):
            if(int(i / 100) % 2 == 0):
                if(int(i / 1000) % 2 == 0):
                    evens.append(i)

print(evens)