#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc
def Pythagorean(sum):
    for i in range(1,sum):
        for j in range(1,sum):
            l=sum-i-j
            if l**2 == i**2+j**2:
                return i*j*l
print(Pythagorean(1000))