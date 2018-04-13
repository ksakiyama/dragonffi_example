import time
start = time.time()

import pydffi

N = 30

c_src = None
with open("cfunc/fibonacci_opt.c") as f:
    c_src = "".join(f.readlines())

F = pydffi.FFI()
CU = F.compile(c_src)

print(int(CU.funcs.f(N)))
print("Time:{}[sec]".format(time.time() - start))
