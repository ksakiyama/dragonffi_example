import time
start = time.time()

N = 30

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1)+f(n-2)


print(f(N))
print("Time:{}[sec]".format(time.time() - start))