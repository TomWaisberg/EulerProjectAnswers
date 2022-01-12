#
import math

sum = 0
sum_of_squares = 0

for i in range(101):
    sum += i
    sum_of_squares += math.pow(i, 2)

print(math.pow(sum, 2) - sum_of_squares)