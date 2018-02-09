import sys
sys.path.append('./build/lib.linux-x86_64-3.6')

import timeit

import xumpy as xp
import numpy as np

SZ = (10000, )

a = xp.ndarray(SZ)
b = xp.ndarray(SZ)

na = np.ndarray(SZ, dtype=np.float64)
nb = np.ndarray(SZ, dtype=np.float64)

def np_add():
	nc = na + nb

def xp_add():
	c = a + b

def get_timeit(cb):
	tr = timeit.Timer(cb)
	NI, elapsed = tr.autorange()
	return min(tr.repeat(3, NI))


def bench():
	global a, b, na, nb
	szs = [3, 10, 100, 1000, 100000, 500000]
	times_np = []
	times_xp = []
	for sz in szs:
		SZ = (sz, )

		a = xp.ndarray(SZ)
		b = xp.ndarray(SZ)

		na = np.ndarray(SZ, dtype=np.float64)
		nb = np.ndarray(SZ, dtype=np.float64)

		times_np.append(get_timeit(np_add))
		times_xp.append(get_timeit(xp_add))

	print(times_np)
	print(times_xp)

bench()