#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

count=2
n=600851475143
while count*count<n:
    while n%count==0:
        n/=count
    count+=1
print(int(n))