"""
Diese Funktion stammt aus:
Langtangen, Hans Petter(2016): A Primer on Scientific Programming with Python,
(= Texts in Computational Science and Engineering, Bd. 6),
Springer: Berlin / Heidelberg, 5. Auflage.
"""

def newton(f, x, dfdx, epsilon=1e-7, N=100, store=False):
    f_value = f(x)
    n = 0
    if store: info = [(x, f_value)]
    while abs(f_value) > epsilon and n <= N:
        dfdx_value = dfdx(x)
        if abs(dfdx_value) < 1e-14:
            raise ValueError(f"Newton: f'({x:g}) = {dfdx_value:g}")
        x = x - f_value/dfdx_value
        n += 1
        f_value = f(x)
        if store: info.append((x, f_value))
    if store:
        return x, info
    else:
        return x, n, f_value