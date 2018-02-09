#include <xtensor/xarray.hpp>
#include <xtensor/xmath.hpp>
#include <xtensor/xeval.hpp>
#include <xtensor/xnoalias.hpp>

using namespace xt;

template <class T>
auto xadd(const xarray<T>& lhs, const xarray<T>& rhs)
{
	xarray<T> ret;
	xt::noalias(ret) = lhs + rhs;
	return ret;
}

template <class T>
xarray<T> xsum(xarray<T>& arr)
{
	return xt::eval(xt::sum(arr, {0}, xt::evaluation_strategy::immediate()));
}

// JUST SOME BOILERPLATE TO CHECK SIMD CONFIG

#ifdef XTENSOR_USE_XSIMD
#ifdef __GNUC__
template <class T>
void print_type(T&& /*t*/)
{
    std::cout << __PRETTY_FUNCTION__ << std::endl;
}
#endif
void print_stats()
{
    std::cout << "USING XSIMD\nSIMD SIZE: " << xsimd::simd_traits<double>::size << "\n\n";
#ifdef __GNUC__
    print_type(xt::xarray<double>());
    print_type(xt::xtensor<double, 2>());
#endif
}
#else
void print_stats()
{
    std::cout << "NOT USING XSIMD\n\n";
};
#endif
