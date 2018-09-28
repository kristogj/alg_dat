from time import time


# Recursive
def get_fib(position):
    return get_fib(position-1) + get_fib(position-2) if position > 1 else position


# Iterative
def get_fib2(position):
    r1 = 1
    r2 = 1
    if position > 1:
        res = r1 + r2
        for x in range(2,position):
            r1 = r2
            r2 = res
            res = r1 + r2
        return res
    return 1


# Big time difference
y = 40
t1 = time()
get_fib(y)
print(time() - t1)
t2 = time()
get_fib2(y)
print(time()-t2)