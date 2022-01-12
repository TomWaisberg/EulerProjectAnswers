# https://projecteuler.net/problem=2

fibonacci = [1, 1]
index = 0
sum = 0
while(fibonacci[-1] < 4000000):
    index += 1
    fibonacci.append(fibonacci[index] + fibonacci[index - 1])
for i in fibonacci:
    if(i % 2 == 0):
        sum += i
print(sum)