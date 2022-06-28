#Find the sum of the digits in the number 100!
import math
x=str(math.factorial(100))
sum=0
for i in x:
    sum+=int(i)
print(sum)