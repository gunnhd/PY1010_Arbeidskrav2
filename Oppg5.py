#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:29:11 2025

@author: gunnhelenedrogset
"""
"""

Oppg 5) Lag et program med en funksjon som tar a og b som inn-argumenter og som så
regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en
halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende
tekst.
"""


import numpy as np

def fun_areal_omkrets(a,b):
    """ 
    Funksjonen beregner totalareal og ytre omkrets av en halvsirkel på en trekant.
    Input a = diameter i halvsirkel = lille katet i trekanten
    Input b = store katet i trekanten
    """
    areal_halvsirkel = (np.pi*(a/2)**2)/2       #A_sirkel = pi*r^2, A_halvsirkel = A_sirkel/2
    areal_trekant= b*a/2                        #g*h/2
    areal = areal_halvsirkel + areal_trekant    #sum areal
    omkrets_halvsirkel = 2*np.pi*(a/2)/2        #2*pi*r / 2
    omkrets_trekant = b + np.sqrt(b**2 + a**2)  #to av sidene
    omkrets = omkrets_halvsirkel + omkrets_trekant
    return areal, omkrets     

a = float(input('Gi inn verdi på a = diameter i halvsirkel og korte katet i trekant: '))
b = float(input('Gi inn verdi på b = den lengste kateten i trekanten: '))
          
svar = fun_areal_omkrets(a, b)

print(f'Den ytre omkretsen er {svar[1]:.1f}, og totalarealet er {svar[0]:.1f}')