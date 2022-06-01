"""
Stellt das Newton-Verfahren graphisch dar.
Die einzelnen Bilder werden zu einer Animation verbunden
(z. B. mit convert -delay 100 ./plots/plot_*.png .Newton.gif).

Zu Beginn eines jeden Durchlaufs wird der Ordner "plots" geleert.

Es können Animationen erstellt werden für verschiedene Funktionen.
Diese müssen unter "f(x)" angegeben werden; in diesem Fall muss auch die 
Ableitungsfunktion "df(x)" angepasst werden.

Es können ebenfalls verschiedenen Werte für den Start des Verfahrens 
angegeben werden.
"""

import matplotlib.pyplot as plt
from Newton import newton
import numpy as np
import glob
import os

def f(x):
    # Funktion, deren Nullstellen bestimmt werden soll (f(x) = 0).
    return x**2 - 3*x - 5

def df(x):
    # df/dx
    return 2*x - 3

def gerade(x0, fx0, dfx0, x):
    """
    legt an f(x0) eine Gerade an;
    berechnet ihre Nullstelle
    """
    return dfx0*(x - x0) + fx0, x0 - fx0/dfx0

def plot_newton(data):
    # prepare data
    data = np.array(data)
    xvals = data[:, 0]
    # compute x-axis
    xmin, xmax = np.min(xvals), np.max(xvals)
    xrange = xmax - xmin
    x = np.linspace(xmin - .1*xrange, xmax + .1*xrange, 100)
    # compute f(x)
    f_x = f(x)
    fmin, fmax = np.min(f_x), np.max(f_x)
    frange = fmax - fmin
    # create plot
    fig, ax = plt.subplots()
    ax.grid(True)
    ax.axis([x[0], x[-1], fmin - .1*frange, fmax + .1*frange])
    ax.plot(x, f_x, 'k--', label='f(x) = $x^2$ - 5x + 3')
    ax.plot([0, 0], [fmin - .1*frange, fmax + .1*frange], 'k-', [x[0], x[-1]], [0, 0], 'k-')
    i = 0
    for x0, fx0 in data:
        dfx0 = df(x0)
        y, y0 = gerade(x0, fx0, dfx0, x)
        ax.text(.15, 1.01, f"f($x_0$) = {fx0:< 7.5f}", color='b', transform=ax.transAxes)
        ax.text(.50, 1.01, f"y = 0 bei x = {y0:< 7.5f}", color='g', transform=ax.transAxes)
        ax.plot(x0, fx0, 'xb', markersize=8, label='f($x_0$)')
        ax.plot(x, y, 'r-', label=f"y = f'($x_0)\cdot x$ + b")
        ax.plot(y0, 0, 'xg', markersize = 8, label='y = 0')
        ax.legend()
        plt.savefig(f"./plots/plot_{i:04d}.png")
        i += 1
        for line in ax.lines[3:]:
            ax.lines.remove(line)
        for text in ax.texts[:]:
            ax.texts.remove(text)

def main():
    for filename in glob.glob('./plots/plot_*.png'):
        os.remove(filename)
    Nullstelle_geraten = 2
    x, info = newton(f, Nullstelle_geraten, df, store=True, N=50)
    plot_newton(info)

if __name__ == '__main__':
    main()