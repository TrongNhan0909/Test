import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

x = sp.symbols("x", real=True)
print("=" * 72)
print("EXERCISE 1 - TINH GIOI HAN")
print("=" * 72)

# (a) lim x->3 |x^2 - x - 7|
fa = sp.Abs(x**2 - x - 7)
print("(a) lim x->3 |x^2 - x - 7| =", sp.limit(fa, x, 3))

# (b) Hai giới hạn một phía khác nhau nên giới hạn hai phía không tồn tại.
fb = sp.Abs(x - 1) / (x**2 - 1)
print("(b) lim x->1- =", sp.limit(fb, x, 1, dir="-"))
print("    lim x->1+ =", sp.limit(fb, x, 1, dir="+"))
print("    Ket luan: gioi han hai phia KHONG TON TAI")

# (c) x-th root of e = e^(1/x)
fc = sp.exp(1/x)
print("(c) lim x->1 nth_root(e) =", sp.limit(fc, x, 1))

fd = (x**4 - 16) / (x - 2)
print("(d) lim x->2 (x^4 - 16)/(x - 2) =", sp.limit(fd, x, 2))

fe = (x**3 - x**2 - 5*x - 3) / (x + 1)**2
print("(e) lim x->-1 =", sp.limit(fe, x, -1))

ff = (x**2 - 9) / (sp.sqrt(x**2 + 7) - 4)
print("(f) lim x->3 =", sp.limit(ff, x, 3))

fg = sp.Abs(x) / sp.sin(x)
print("(g) lim x->1 |x|/sin(x) =", sp.limit(fg, x, 1))
print("    Gia tri gan dung =", float(sp.limit(fg, x, 1)))

fh = (1 - sp.cos(x)) / (x * sp.sin(x))
print("(h) lim x->0 =", sp.limit(fh, x, 0))

fi = 2*x**2 / (3 - 3*sp.cos(x))
print("(i) lim x->0 =", sp.limit(fi, x, 0))

fj = ((x + 3) / (x - 1))**x
print("(j) lim x->oo =", sp.limit(fj, x, sp.oo))

fk = (1 - 2/(3 + x))**x
print("(k) lim x->oo =", sp.limit(fk, x, sp.oo))

# x-th root of 1/x = (1/x)^(1/x), for x -> +infinity
fl = (1/x)**(1/x)
print("(l) lim x->oo =", sp.limit(fl, x, sp.oo))

fm = (-x**(sp.Rational(1, 3)) + (1 + x)**(sp.Rational(1, 3))) / (
    -sp.sqrt(x) + sp.sqrt(1 + x)
)
print("(m) lim x->oo =", sp.limit(fm, x, sp.oo))

# Gamma(x+1) extends factorial to real x; integer factorial has same limit.
print("(n) lim x->oo x!/x^x = 0 (the limit from Stirling's formula)")


print("\n" + "=" * 72)
print("EXERCISE 2 - VE DO THI CAC HAM O EXERCISE 1")
print("=" * 72)
print("Luu y: cac ham co mau bang 0 se bi loai diem khong xac dinh.")
print("Cac ham co |x| hoac can bac hai duoc ve tren mien hop le.")

# Các hàm đại diện; khoảng vẽ được chọn để thấy hình dạng quanh điểm giới hạn.
plot_specs = [
    ("E1a_abs", lambda t: np.abs(t**2 - t - 7), -1, 5, "y = |x^2 - x - 7|"),
    ("E1b_abs_ratio", lambda t: np.abs(t-1)/(t**2-1), -1.5, 3, "y = |x-1|/(x^2-1)"),
    ("E1d", lambda t: (t**4-16)/(t-2), -1, 4, "y = (x^4-16)/(x-2)"),
    ("E1e", lambda t: (t**3-t**2-5*t-3)/(t+1)**2, -3, 1, "y = (x^3-x^2-5x-3)/(x+1)^2"),
    ("E1f", lambda t: (t**2-9)/(np.sqrt(t**2+7)-4), -2.5, 5, "y = (x^2-9)/(sqrt(x^2+7)-4)"),
    ("E1g", lambda t: np.abs(t)/np.sin(t), 0.1, 3, "y = |x|/sin(x)"),
    ("E1h", lambda t: (1-np.cos(t))/(t*np.sin(t)), -2, 2, "y = (1-cos(x))/(x sin(x))"),
    ("E1i", lambda t: 2*t**2/(3-3*np.cos(t)), -2, 2, "y = 2x^2/(3-3cos(x))"),
]
for name, func, lo, hi, title in plot_specs:
    t = np.linspace(lo, hi, 2500)
    with np.errstate(all="ignore"):
        y = func(t)
    y = np.asarray(y, dtype=float)
    y[~np.isfinite(y)] = np.nan
    y[np.abs(y) > 100] = np.nan
    plt.figure(figsize=(7, 4))
    plt.plot(t, y, label=title)
    plt.axhline(0, linewidth=0.7)
    plt.axvline(0, linewidth=0.7)
    plt.grid(True)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.tight_layout()
    plt.savefig(name + ".png", dpi=150)
    plt.close()
    print("Da luu do thi:", name + ".png")

# Các giới hạn ở vô cực: vẽ trên khoảng dương đủ rộng
inf_specs = [
    ("E1j", lambda t: ((t+3)/(t-1))**t, 3, 30, "y = ((x+3)/(x-1))^x"),
    ("E1k", lambda t: (1-2/(3+t))**t, 1, 30, "y = (1-2/(x+3))^x"),
    ("E1l", lambda t: (1/t)**(1/t), 1, 30, "y = (1/x)^(1/x)"),
    ("E1m", lambda t: (-(t**(1/3))+(1+t)**(1/3))/(-np.sqrt(t)+np.sqrt(1+t)), 1, 100, "y = (-cuberoot(x)+cuberoot(1+x))/(-sqrt(x)+sqrt(1+x))"),
]
for name, func, lo, hi, title in inf_specs:
    t = np.linspace(lo, hi, 2500)
    with np.errstate(all="ignore"):
        y = func(t)
    y = np.asarray(y, dtype=float)
    y[~np.isfinite(y)] = np.nan
    plt.figure(figsize=(7, 4))
    plt.plot(t, y)
    plt.grid(True)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.savefig(name + ".png", dpi=150)
    plt.close()
    print("Da luu do thi:", name + ".png")

print("\n" + "=" * 72)
print("EXERCISE 3 - GIOI HAN MOT PHIA")
print("=" * 72)
f31 = 1 / (1 + 2**(1/x))
print("3.1 f(x)=1/(1+2^(1/x))")
print("  lim x->0+ =", sp.limit(f31, x, 0, dir="+"))
print("  lim x->0- =", sp.limit(f31, x, 0, dir="-"))
print("  lim x->0  KHONG TON TAI vi gioi han trai = 1 khac gioi han phai = 0.")

f32 = (x**2 + x) / sp.sqrt(x**3 + x**2)
print("3.2 f(x)=(x^2+x)/sqrt(x^3+x^2)")
print("  Mien xac dinh gan 0: x^2(x+1)>0, nen x != 0 va x > -1.")
print("  lim x->0+ =", sp.limit(f32, x, 0, dir="+"))
print("  lim x->0- =", sp.limit(f32, x, 0, dir="-"))
print("  lim hai phia KHONG TON TAI vi gioi han trai = -1, phai = 1.")

# Vẽ Exercise 3
t = np.linspace(0.02, 2, 1500)
plt.figure(figsize=(7,4))
plt.plot(t, 1/(1+2**(1/t)))
plt.title("Exercise 3.1: f(x)=1/(1+2^(1/x)), x > 0")
plt.xlabel("x"); plt.ylabel("f(x)"); plt.grid(True); plt.tight_layout()
plt.savefig("E3a_right.png", dpi=150); plt.close()
t = np.linspace(-0.95, -0.02, 1500)
plt.figure(figsize=(7,4))
plt.plot(t, (t**2+t)/np.sqrt(t**3+t**2))
plt.title("Exercise 3.2: f(x)=(x^2+x)/sqrt(x^3+x^2), -1 < x < 0")
plt.xlabel("x"); plt.ylabel("f(x)"); plt.grid(True); plt.tight_layout()
plt.savefig("E3b_left_domain.png", dpi=150); plt.close()
print("Da luu do thi E3a_right.png, E3b_left_domain.png")


print("\n" + "=" * 72)
print("EXERCISE 4 - HAM SO CHO TUNG KHOANG")
print("=" * 72)
print("f(x)=0 neu x<=0; f(x)=sin(1/x) neu x>0")
print("1. lim x->0+ sin(1/x) KHONG TON TAI (dao dong).")
print("2. lim x->0- f(x) = 0.")
print("3. lim x->0 f(x) KHONG TON TAI vi gioi han phai khong ton tai.")
t_left = np.linspace(-2, 0, 1000)
t_right = np.linspace(0.015, 2, 4000)
plt.figure(figsize=(7,4))
plt.plot(t_left, np.zeros_like(t_left), label="x <= 0: f(x)=0")
plt.plot(t_right, np.sin(1/t_right), label="x > 0: f(x)=sin(1/x)")
plt.title("Exercise 4: ham so tung khoang")
plt.xlabel("x"); plt.ylabel("f(x)"); plt.grid(True); plt.legend(); plt.tight_layout()
plt.savefig("E4_piecewise.png", dpi=150); plt.close()
print("Da luu do thi E4_piecewise.png")


print("\n" + "=" * 72)
print("EXERCISE 5 - CHUNG MINH LIEN TUC TAI c")
print("=" * 72)
print("(a) f(x)=x^2-7, c=1")
print("  f(1) =", (1**2)-7)
print("  lim x->1 f(x) =", sp.limit(x**2-7, x, 1))
print("  Vi gioi han = f(1) = -6, ham lien tuc tai x=1.")
print("(b) f(x)=sqrt(2x-3), c=2")
print("  f(2) =", math.sqrt(2*2-3))
print("  lim x->2 f(x) =", sp.limit(sp.sqrt(2*x-3), x, 2))
print("  Vi gioi han = f(2) = 1, ham lien tuc tai x=2.")


print("\n" + "=" * 72)
print("EXERCISE 6 - KIEM TRA TINH LIEN TUC")
print("=" * 72)
print("(a) Theo anh: g(x)=(x^2-x-6)/(x-3) khi x!=0; g(0)=5.")
print("    Tai x=0: lim g(x)=(-6)/(-3)=2, nhung g(0)=5 => khong lien tuc tai 0.")
print("    Luu y: de bai con bi loi mien xac dinh tai x=3 vi mau bang 0 ma dieu kien chi ghi x!=0.")
print("    Bieu thuc rut gon thanh x+2 khi x!=3; tai x=3 ham khong xac dinh.")
print("(b) f(x)=(x^3-8)/(x^2-4) neu x!=2,-2; f(2)=3; f(-2)=4.")
fb6 = (x**3-8)/(x**2-4)
print("    lim x->2 =", sp.limit(fb6, x, 2), "; f(2)=3 => lien tuc tai 2.")
print("    Tai x=-2 mau bang 0 nhung tu so = -16 != 0, nen co tiem can dung va khong lien tuc tai -2.")
print("(c) Anh khong hien ro gia tri f(2) o dong thu hai; bieu thuc khi x!=2 co gioi han:")
fc6 = (x**2-x-2)/(x-2)
print("    lim x->2 (x^2-x-2)/(x-2) =", sp.limit(fc6, x, 2), "= 3.")
print("    f(2)=1 theo de bai, khac gioi han 3 => khong lien tuc tai 2.")
print("(d) f(x)=1/x^2 neu x!=0; f(0)=1.")
print("    lim x->0 1/x^2 = +oo, khong bang f(0)=1 => khong lien tuc tai 0.")


print("\n" + "=" * 72)
print("EXERCISE 7 - TIM DIEM GIAN DOAN")
print("=" * 72)
f71 = (x**2-x-2)/(x-2)
print("7.1 f(x)=(x^2-x-2)/(x-2)")
print("    Phan tich tu so: (x-2)(x+1); ham rut gon thanh x+1 khi x!=2.")
print("    Gian doan tai x=2 (gian doan co the khac phuc); lim =", sp.limit(f71, x, 2))
f72 = (x**2-2*x-3)/(2*x-6)
print("7.2 f(x)=(x^2-2x-3)/(2x-6)")
print("    Mau bang 0 tai x=3; tu so tai 3 = 0, nen gian doan co the khac phuc.")
print("    Rut gon = (x+1)/2 khi x!=3; lim x->3 =", sp.limit(f72, x, 3))


print("\n" + "=" * 72)
print("EXERCISE 8 - KIEM TRA LIEN TUC TREN [-1,1]")
print("=" * 72)
f8 = 1 - sp.sqrt(1-x**2)
print("f(x)=1-sqrt(1-x^2), mien x thuoc [-1,1].")
print("Tai x=-1: f(-1) =", f8.subs(x,-1), "; gioi han phai =", sp.limit(f8, x, -1, dir="+"))
print("Tai x=1:  f(1)  =", f8.subs(x,1), "; gioi han trai =", sp.limit(f8, x, 1, dir="-"))
print("Trong (-1,1), ham la hop cua cac ham lien tuc.")
print("Tai hai dau mut, gioi han mot phia bang gia tri ham; do do lien tuc tren [-1,1].")
t = np.linspace(-1, 1, 1000)
plt.figure(figsize=(7,4))
plt.plot(t, 1-np.sqrt(1-t**2))
plt.title("Exercise 8: f(x)=1-sqrt(1-x^2), -1 <= x <= 1")
plt.xlabel("x"); plt.ylabel("f(x)"); plt.grid(True); plt.tight_layout()
plt.savefig("E8_continuous.png", dpi=150); plt.close()
print("Da luu do thi E8_continuous.png")


print("\n" + "=" * 72)
print("EXERCISE 9 - HE SO GOC CAT TUYEN PQ")
print("=" * 72)
print("P=(1,0), Q=(x, sin(10*pi/x)); slope m=(sin(10*pi/x)-0)/(x-1).")
xs = [2, 1.5, 1.4, 1.3, 1.2, 1.1, 0.5, 0.6, 0.7, 0.8, 0.9]
print(f"{'x':>8} {'sin(10*pi/x)':>18} {'slope PQ':>18}")
for xv in xs:
    yv = math.sin(10*math.pi/xv)
    slope = yv/(xv-1)
    print(f"{xv:8.2f} {yv:18.8f} {slope:18.8f}")
print("Chu y: x=1 khong nam trong danh sach vi cong thuc he so goc chia cho x-1.")


print("\n" + "=" * 72)
print("EXERCISE 10 - TIM L DE HAM LIEN TUC")
print("=" * 72)
print("(a) f(x)=sin(x)/x neu x!=0; f(0)=L.")
print("    L = lim x->0 sin(x)/x =", sp.limit(sp.sin(x)/x, x, 0))
print("(b) f(x)=(x^2+x-6)/(x^2-4) neu x!=2; f(2)=L.")
f10b = (x**2+x-6)/(x**2-4)
print("    Phan tich: (x+3)(x-2)/((x-2)(x+2)) = (x+3)/(x+2).")
print("    L = lim x->2 =", sp.limit(f10b, x, 2))