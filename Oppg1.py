#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 09:53:45 2025

@author: gunnhelenedrogset

"""
"""
Oppg 1) Du skal her lage et program som skal starter med
alder = int(input('Hvilket år er du født? ') )
Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive
svaret til skjerm med passende tekst.
"""

alder = int(input('Hvilket år er du født? ') )

# calculate how old the person will be during 2024
age_in_2024 = 2024 - alder

print(f'Du som er født i {alder}, vil fylle {age_in_2024} år i løpet av 2024')