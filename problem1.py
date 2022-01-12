# https://projecteuler.net/problem=1

sum = 0
for i in range(1000, 0, -1):
    if(i%3 == 0 or i%5 == 0):
        sum += i
print(sum)