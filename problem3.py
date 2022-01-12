# https://projecteuler.net/problem=3

num = 600851475143
factors = [71, 839, 1471, 6857, 59569, 104441, 486847, 1234169, 5753023, 10086647, 87625999, 408464633]
for i in range(408464634, num):
    print(i)
    if(num % i == 0):
        factors.append(i)
