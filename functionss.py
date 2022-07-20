"""Functions are of three types

1. In built functions ex int(), str(), bool()
2. model functions  ex when related function and related varible is stored in same file that is call model funciton

ex math module
3. user-defined functions defined by us ex def function_name(parameters):"""

from math import *
#print(dir(math))
#['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
print(sqrt(16))
#4.0
#********************************************************************************

def print_sum(first, second):
    print(first+second)


print_sum(1,2)
#3
def print_sum(first, second=4):
    print(first+second)


print_sum(1)
#5