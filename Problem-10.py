#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
#Find the sum of all the primes below two million.

import sympy
primes= sympy.primerange(1,2000000)
print(sum(primes))