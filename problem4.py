# https://projecteuler.net/problem=4

palindromes = []
for x in range (100, 1000):
    for y in range (100, 1000):
        if(str(x*y) == str(x*y)[::-1]):
            palindromes.append(x*y)
palindromes.sort()
print(palindromes[-1])
