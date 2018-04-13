# DragonFFI Examples
[DragonFFI](https://github.com/aguinet/dragonffi) a C Foreign Function Interface (FFI) library written in C++ and based on Clang/LLVM.

I coded some python examples using DragonFFI.

## Motivation
LLVM Project announced about DragonFFI on [this post](http://blog.llvm.org/2018/03/dragonffi-ffijit-for-c-language-using.html). So I tried!

## My Setting
* Runtime
  * Python 3.6.3 :: Anaconda, Inc.
* Installation
  * ```pip install pydffi```


## Easy Benchmark

### Fibonacci
```
$ python fib_nrm.py 
Time:0.3381009101867676[sec]
$ python fib_opt.py 
Time:5.2928924560546875e-05[sec]
$ python call_fib_from_c_nrm.py 
Time:0.049577951431274414[sec]
$ python call_fib_from_c_opt.py 
Time:0.04542684555053711[sec]
```

### Matmul
```
$ python matmul.py
Python:7.10671[sec]
C(FFI):0.03292[sec]
numpy :0.02811[sec]
```