#Question 3

n = input('Enter your number: ')
dictionary = {}

for i in range(1, int(n) + 1):
    dictionary[i] = int(i) * int(i)

print(dictionary)

