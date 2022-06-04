#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i = 1
for l in (range(1, 21)):
    if i % l > 0:
        for j in range(1, 21):
            if (i*j) % l == 0:
                i *= j
                break
print (i)