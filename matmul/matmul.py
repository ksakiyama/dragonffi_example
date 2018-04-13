import random
import pydffi
import numpy as np

N = 4

A = [random.random() for _ in range(N) for _ in range(N)]
B = [random.random() for _ in range(N) for _ in range(N)]
C = [0.0 for _ in range(N) for _ in range(N)]

c_src = None
with open("cfunc/matmul.c") as f:
    c_src = "".join(f.readlines())

FFI = pydffi.FFI()
CU = FFI.compile(c_src)

arr_A = pydffi.CArrayObj(FFI.arrayType(FFI.DoubleTy, N*N))
arr_B = pydffi.CArrayObj(FFI.arrayType(FFI.DoubleTy, N*N))
arr_C = pydffi.CArrayObj(FFI.arrayType(FFI.DoubleTy, N*N))
for i in range(N*N):
    arr_A.set(i, A[i])
    arr_B.set(i, B[i])
    arr_C.set(i, 0.0)

CU.funcs.matmul(arr_A, arr_B, arr_C, N)

for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i * N + j] += A[i * N + k] * B[k * N + j]

print("{:.8f}".format(arr_C.get(0)))
print("{:.8f}".format(C[0]))
print("{:.8f}".format(arr_C.get(5)))
print("{:.8f}".format(C[5]))
print("{:.8f}".format(arr_C.get(10)))
print("{:.8f}".format(C[10]))
print("{:.8f}".format(arr_C.get(15)))
print("{:.8f}".format(C[15]))
