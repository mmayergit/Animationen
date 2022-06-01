"""
Funktionsweise wie die Newtonmethode.
Der einzige Unterschied ist, dass die Ableitung nicht explizit angegeben wird,
sondern in der Zeile dfdx = ... lokal berechnet wird.

Dafür ist jetzt ein zweiter Anfangswert anzugeben, der für die Ableitung benötigt wird.
"""

from math import sin

def secant(f, x0, x1, epsilon=1e-7, N=100, store=False):
    x = x1
    f_value = f(x)
    n = 0
    x_nm2 = x0
    if store: info = [(x, f_value)]
    while abs(f_value) > epsilon and n <= N:
        dfdx = (f_value - f(x_nm2))/(x - x_nm2)
        if abs(dfdx) < 1e-14:
            raise ValueError(f"Newton: f'({x:g}) = {dfdx:g}")
        x_nm2 = x
        x = x - f_value/dfdx
        n += 1
        f_value = f(x)
        if store: info.append((x, f_value))
    if store:
        return x, info
    else:
        return x, n, f_value

def g(x):
    return x**5 - sin(x)

def main():
    x0, x1 = 2.5, 3
    x, info = secant(g, x0, x1, store=True)
    print('root: ', x)
    for i in range(len(info)):
        print(f"Iteration {i:3d}: f({info[i][0]:g}) = {info[i][1]:g}")

if __name__ == '__main__':
    main()