import time
start = time.time()

N = 30

memo = [0] * 100

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if memo[n]:
        return memo[n]

    m = f(n-1)+f(n-2)
    memo[n] = m
    return m


print(f(N))
print("Time:{}[sec]".format(time.time() - start))
