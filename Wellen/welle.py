"""
Es werden Plots für ein Gif erstellt, das die Bewegung einer Welle
veranschaulicht.
Das array "points" legt fest, welche Punkte in der Darstellung einzeln
verfolgt werden können.

Die Bilder können z. B. über 
convert -delay 10 ./plots/plot_*.png .Welle.gif
verbunden werden.
"""

import matplotlib.pyplot as plt
import numpy as np
import glob
import os

def main():
    # Entfernen der alten Dateien
    for filename in glob.glob('./plots/plot_*.png'):
        os.remove(filename)
    # Periodenlänge und -dauer
    per_len = 2*np.pi
    per_dur = 2*np.pi
    # Ortsraum und Zeitraum der Simulation
    xmin = -per_len
    xmax = per_len
    tmin = 0
    tmax = per_dur
    x = np.linspace(xmin, xmax, int(1e4))
    t = np.linspace(tmin, tmax, int(1e2))
    points = np.arange(xmin, xmax, np.pi/4)
    # Diagramm erstellen
    fig, ax = plt.subplots()
    ax.plot([xmin, xmax], [0, 0], '-k')
    ax.plot([0, 0], [-1, 1], '-k')
    xticks = [0]
    yticks = [-1, 1]
    yticklbl = [r'$\xi_{min}$', r'$\xi_{max}$']
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklbl)
    # Zähler für Bildnamen
    i = 0
    # Berechnung der Welle und Erstellen der Plots
    for t_ in t:
        welle = np.sin(x - t_)
        points_amp = np.sin(points - t_)
        for point, amp in zip(points, points_amp):
            ax.plot([point, point], [0, amp], linestyle = '--', color = 'tab:red', linewidth = 1)
        ax.plot(x, welle, ':', color = 'tab:blue', linewidth = 2)
        ax.plot(points, points_amp, '.', color = 'tab:orange', markersize = 10)
        plt.savefig(f"./plots/plot_{i:04d}.png")
        i += 1
        for line in ax.lines[2:]:
            ax.lines.remove(line)
        for text in ax.texts[:]:
            ax.texts.remove(text)

if __name__ == '__main__':
    main()