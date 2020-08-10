#Question 1

start = 2000
stop = 3200

list1 = []

for x in range(start, stop + 1):
    if (x % 7 == 0) and (x % 5 != 0): 
        list1.append(str(x))
        
print(list1)       