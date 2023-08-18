#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3+3+5+4+4=19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example,342 (three hundred and forty-two) contains 23 letters and 115 
#(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def writing_numbers(n: int) -> str:
    ones=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen", "nineteen"]
    tens=[None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if 0<=n<20:
        return ones[n]
    elif 20<=n<=90 and n%10==0:
        return tens[n//10]
    elif 20<n<100:
        return tens[n//10]+" "+ones[n%10]
    elif 100<=n<1000 and n%100==0:
        return ones[n//100]+" hundred"
    elif 100<n<1000:
        return ones[n//100]+" hundred and "+ str(writing_numbers(n%100))
    elif 1000 < n < 10000:
        pass
    elif n == 1000:
        return "one thousand"

print(writing_numbers(800))
count=0
for i in range (1,1001):
    words=str(writing_numbers(i)).replace(" ","")
    count+=len(words)
print(count)
