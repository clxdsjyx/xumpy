from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from distutils.extension import Extension

setup(
	name = "xumpy",
    ext_modules=cythonize([Extension(
        "xumpy",
        ["src/xumpy.pyx"],  # our Cython source
        language="c++",  # generate C++ code
        include_dirs=["/usr/local/include"],
        define_macros=[("XTENSOR_USE_XSIMD", "1")],
        extra_compile_args=["-O3", "-march=native"]
    )])
    # cmdclass={
    #     'build_ext': build_ext
    # }
)
