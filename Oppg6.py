#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 13:32:47 2025

@author: gunnhelenedrogset
"""
"""

Oppg 6) Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥2− 5, for x på intervallet [-10,10].
Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet
[-10,10].
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
f_x = -(x)**2 - 5

plt.close()
plt.figure(1)
plt.plot(x, f_x)
plt.savefig('funksjonsplott.pdf')
plt.show()

