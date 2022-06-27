#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
f = open("Problem-13.txt", "r")
x=(f.read()).split()
sum=0
for i in x:
    sum+=int(i)
print(str(sum)[:10])