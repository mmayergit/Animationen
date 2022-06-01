"""
Gesucht wird die Nullstelle einer Funktion f im Intervall [a, b].
Ist f(a)*f(b) < 0, so muss im Intervall ein Nulldurchgang liegen.
Das Intervall wird halbiert (m). Wenn der Durchgang nun in der linken
Hälft liegt, wird dieses Intervall als Ausgangsintervall benutzt, ansonsten 
wird das rechte Intervall genommen.

Dieses Verfahren wird wiederholt, bis die eingestellte Genauigkeit erreicht ist.
"""


def bisection(f, a, b, epsilon=1e-7, store=False):
    f_a = f(a)
    if store:
        info = []
    if f_a*f(b) > 0:
        raise ValueError('Intervallgrenzen anpassen!')
    i = 0
    while b-a > epsilon:
        i += 1
        mitte = (a + b)/2
        f_mitte = f(mitte)
        if f_a*f_mitte <= 0:
            b = mitte
        else:
            a = mitte
            f_a = f_mitte
        if store:
            info.append((mitte, f_mitte))
    if store:
        return mitte, info
    else:
        return mitte, f_mitte

def main():
    print(bisection(lambda x: x**2 - x - 2, -3, 0))

if __name__ == '__main__':
    main()