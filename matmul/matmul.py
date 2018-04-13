import time
import random
import pydffi
import numpy as np

N = 256

# random values
A = [random.random() for _ in range(N) for _ in range(N)]
B = [random.random() for _ in range(N) for _ in range(N)]
C = [0.0 for _ in range(N) for _ in range(N)]

# read c source
c_src = None
with open("cfunc/matmul.c") as f:
    c_src = "".join(f.readlines())

# initialize
FFI = pydffi.FFI()
CU = FFI.compile(c_src)

# create array objects & set values
arr_A = pydffi.CArrayObj(FFI.arrayType(FFI.DoubleTy, N*N))
arr_B = pydffi.CArrayObj(FFI.arrayType(FFI.DoubleTy, N*N))
arr_C = pydffi.CArrayObj(FFI.arrayType(FFI.DoubleTy, N*N))
for i in range(N*N):
    arr_A.set(i, A[i])
    arr_B.set(i, B[i])
    arr_C.set(i, 0.0)

# execute python matmul
start = time.time()
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i * N + j] += A[i * N + k] * B[k * N + j]
print("Python:{:.5f}[sec]".format(time.time() - start))

# execute c matmul
start = time.time()
CU.funcs.matmul(arr_A, arr_B, arr_C, N)
print("C(FFI):{:.5f}[sec]".format(time.time() - start))

# execute numpy matmul
np_A = np.array(A).reshape(N, N)
np_B = np.array(B).reshape(N, N)
start = time.time()
np_C = np.matmul(np_A, np_B)
print("numpy :{:.5f}[sec]".format(time.time() - start))
