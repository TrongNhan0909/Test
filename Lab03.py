import math
import numpy as np

# (a) f(x) = sqrt(x)
def f_a(x):
    return math.sqrt(x)

# (b) f(x) = cbrt(x) (căn bậc ba)
def f_b(x):
    return np.cbrt(x)

# (c) f(x) = x^(2/3)
def f_c(x):
    return x ** (2 / 3)

# (d) f(x) = x^3/3 - x^2/2 - 2x + 1/3
def f_d(x):
    return (x**3)/3 - (x**2)/2 - 2*x + 1/3

# (e) f(x) = (2x^2 - 3) / (7x + 4)
def f_e(x):
    return (2*x**2 - 3) / (7*x + 4)

# (f) f(x) = (5x^2 + 8x - 3) / (3x^2 + 2)
def f_f(x):
    return (5*x**2 + 8*x - 3) / (3*x**2 + 2)

# (g) f(x) = sin(x)
def f_g(x):
    return math.sin(x)

# (h) f(x) = cos(x)
def f_h(x):
    return math.cos(x)

# (i) f(x) = 3^x
def f_i(x):
    return 3**x

# (j) f(x) = 10^(-x)
def f_j(x):
    return 10**-x

# (k) f(x) = e^x
def f_k(x):
    return math.exp(x)

# (l) f(x) = log2(x)
def f_l(x):
    return math.log2(x)

# (m) f(x) = log10(x)
def f_m(x):
    return math.log10(x)

# (n) f(x) = ln(x)
def f_n(x):
    return math.log(x)
so_test = 8  # Thử nghiệm với số 8

print("Kết quả câu a (Căn bậc 2 của 8) là:", f_a(so_test))
print("Kết quả câu b (Căn bậc 3 của 8) là:", f_b(so_test))
print("Kết quả câu c (8 mũ 2/3) là:", f_c(so_test))