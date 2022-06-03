#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
multiples=[]
palindromes=[]
for i in range (100,1000):
    for j in range (100,1000):
        n=str(i*j)  
        if n==n[::-1]:
            palindromes.append(int(n))

print(max(palindromes))
