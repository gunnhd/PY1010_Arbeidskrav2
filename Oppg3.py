#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 10:19:40 2025

@author: gunnhelenedrogset
"""
"""

Oppg 3) Lag et program med en funksjon som regner om fra grader til radianer.
Programmet skal starte med:
import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
Radiantallet til vinkelen regnes så ut ved følgende formel: v_rad = v_grad*np.pi/180
Resultatet v_rad skrives til skjerm med passende tekst og verdi.
Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415....

"""

import numpy as np
v_grad = float(input('Skriv inn gradtallet: ' ))
v_rad = v_grad*np.pi/180

print(f'{v_grad} grader, tilsvarer {v_rad:.2f} radianer')