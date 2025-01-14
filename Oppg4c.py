#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 10:23:47 2025

@author: gunnhelenedrogset
"""
"""

c) Lag et program som ber brukeren skrive inn info om et nytt land (altså et land som
ikke allerede finnes i dictionaryen data). Videre skal brukeren oppgi hovedstad og
antall innbyggere for det «nye» landet. Programmet skal så utvide/oppdatere
dictionaryen med den nye informasjonen. Dictionaryen data skrives så til skjerm.

"""

data = {
        "Norge" : {
                  "hovedstad" : "Oslo", 
                  "innbyggere" : 0.634
                  },
                   
        "England" : {
                  "hovedstad" : "London", 
                  "innbyggere" : 8.982
                  },
        "Frankrike" : {
                  "hovedstad" : "Paris", 
                  "innbyggere" : 2.161
                  },
        "Italia" : {
                  "hovedstad" : "Roma", 
                  "innbyggere" : 2.873
                  }
        }
print(f'Original dictionary: {data}')


nytt_land = input('Skriv inn navn på nytt land: ')
ny_hovedstad = input(f'Skriv inn navnet på hovedstaden i {nytt_land} :')
nytt_innbyggertall = float(input(f'Skriv inn innbyggertallet i {ny_hovedstad}: '))

if nytt_land not in data:
   data[nytt_land] = {
      "hovedstad" : ny_hovedstad, 
      "innbyggere" : nytt_innbyggertall
      }
   print(f'Oppdatert dictionary: {data}')
else:
    print(f'Landet {nytt_land} er allerede i lista!')