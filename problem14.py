# https://projecteuler.net/problem=14

def do_collatz(start):
    reps = 1
    while(start != 1):
        if(start % 2 == 0):
            start /= 2
        else:
            start = start * 3 + 1
        reps += 1
        
    return reps

max_reps = 0
max_reps_number = 0
for i in range(1, 1000000):
    if(do_collatz(i) > max_reps):
        max_reps = do_collatz(i)
        max_reps_number = i
    print(f"{i} : {do_collatz(i)}")

print(f"{max_reps_number} : {max_reps}")
