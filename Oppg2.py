#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 10:00:21 2025

@author: gunnhelenedrogset

"""
"""

Oppg 2) Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. Lag et
program som tar inn antall elever fra konsollen ved
antall_elever = int(input('Skriv inn antall elever:' ))
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive
svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe
5).
Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. Hvordan kan
sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?

"""

antall_elever = int(input('Skriv inn antall elever: ' ))

antall_elever_pr_pizza = 4

# calculate the number of whole pizzas and 'rest'
x = divmod(antall_elever, antall_elever_pr_pizza)
hele_pizza = x[0]
rest_biter = x[1] 
if rest_biter == 0:
   ant_pizza = x[0]
else :
   ant_pizza = hele_pizza + 1

print(f'Dersom det er {antall_elever} elever i klassen, så må det handles inn {ant_pizza} pizza')