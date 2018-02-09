from libcpp.vector cimport vector

cdef extern from "<xtensor/xarray.hpp>" namespace "xt" nogil:
    cdef cppclass xarray[T, ALLOCATOR=*]:
        ctypedef T value_type
        ctypedef ALLOCATOR allocator_type

        ctypedef size_t size_type
        ctypedef ptrdiff_t difference_type

        xarray() except +
        xarray(vector[size_t]&, T value)

        T& operator[](size_type)

        vector[size_type]& shape()

cdef extern from "xsupport.hpp" nogil:
    cdef xarray[double] xadd(xarray[double]&, xarray[double]&)
    cdef xarray[double] xsum(xarray[double]&)
    cdef void print_stats()

cdef class ndarray:
    cdef xarray[double] arr

    def __cinit__(self, vector[size_t] shape = []):
        self.arr = xarray[double](shape, 1)

    def __getitem__(self, size_t idx):
        return self.arr[idx]

    def __setitem__(self, size_t idx, int val):
        self.arr[idx] = val

    def shape(self):
        return self.arr.shape()

    def __add__(ndarray self, ndarray rhs):
        ret = ndarray()
        ret.arr = xadd(self.arr, rhs.arr)
        return ret

def print_info():
    print_stats()

def sum(ndarray lhs):
    ret = ndarray()
    ret.arr = xsum(lhs.arr)
    return ret