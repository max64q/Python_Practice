#Question 2

num = input("Enter value to be factorializred: ")
out = 1

for i in range(int(num), 0, -1):
    out *= i
    
print(out)

