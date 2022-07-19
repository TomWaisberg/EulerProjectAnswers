#https://projecteuler.net/problem=25
fibonacci = [1, 1]
index = 0

while(not len(str(fibonacci[-1])) == 1000):
    index += 1
    fibonacci.append(fibonacci[index] + fibonacci[index - 1])
    print(f"{index} : {fibonacci[-1]}")

print(index + 2)