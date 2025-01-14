#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 10:20:29 2025

@author: gunnhelenedrogset
"""
"""

b) Lag et program som ber brukeren skrive inn et land (eksempelvis England).
Programmet skal på bakgrunn av dette skrive ut følgende setning:
London er hovedstaden i England og det er 8.982 mill. innbyggere i London

"""

data = {
        "Norge" : {
                  "hovedstad" : "Oslo", 
                  "innbyggere" : 0.634},
                   
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

# Les inn navn på landet
landet = input('Skriv inn land: ')
if landet in data:
    hovedstaden = data[landet]["hovedstad"]
    innbyggertall = data[landet]["innbyggere"]
    print(f'{hovedstaden} er hovedstaden i {landet} og det er {innbyggertall} millioner innbyggere i {hovedstaden}')
else:
    print(f'{landet} er ikke i lista, velg blant {data.keys()}')