#Question 6
import math

C = 50
H = 30

values = input("Enter comma seperated list: ")
l = values.split(',')
out = []

for i in l:
    Q = math.sqrt((2 * C * float(i)) / H)
    out.append(Q)

print(out)

''''
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)

''''