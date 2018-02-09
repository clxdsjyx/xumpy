import sys
sys.path.append('./build/lib.linux-x86_64-3.6')

import timeit
import perf
import xumpy as xp
import numpy as np

SZ = (100000, )

a = xp.ndarray(SZ)
b = xp.ndarray(SZ)

na = np.ndarray(SZ, dtype=np.float64)
nb = np.ndarray(SZ, dtype=np.float64)

def xp_alloc():
	allc = xp.ndarray(SZ)

def np_alloc():
	allc = np.ndarray(SZ, dtype=np.float64)

def np_add():
	nc = na + nb

def xp_add():
	c = a + b

def get_timeit(cb):
	tr = timeit.Timer(cb)
	NI, elapsed = tr.autorange()
	return (min(tr.repeat(3, NI)) / NI) * (10 ** 9)

def bench():
	global a, b, na, nb
	szs = [3, 10, 100, 1_000, 10_000, 100_000, 500_000]
	times_np = []
	times_xp = []
	for sz in szs:
		SZ = (sz, )

		a = xp.ndarray(SZ)
		b = xp.ndarray(SZ)

		na = np.ndarray(SZ, dtype=np.float64)
		nb = np.ndarray(SZ, dtype=np.float64)

		times_xp.append(get_timeit(xp_add))
		times_np.append(get_timeit(np_add))
		print(f"Size: {sz}")
		print(f"  np: {times_np[-1]}")
		print(f"  xp: {times_xp[-1]}")
		print("---------------------------------\n")

	print(times_np)
	print(times_xp)

bench()

# print(timeit.timeit(xp_add, number=10000))
# print(timeit.timeit(np_add, number=10000))

# print(timeit.timeit(xp_alloc, number=10000))
# print(timeit.timeit(np_alloc, number=10000))
# print(timeit.timeit(xp.sum(a), number=10000))
# print(timeit.timeit(np.sum(a, 1), number=10000))
