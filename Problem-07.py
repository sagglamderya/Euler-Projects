#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import math
primes=[2]
num=3
while len(primes)<10001:
    if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
        primes.append(num)
    num+=2
print(primes[10000])