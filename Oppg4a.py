#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 10:22:51 2025

@author: gunnhelenedrogset
"""
"""

Oppg 4)
a) Opprett en dictionary som gitt under. Dictionaryen har ulike land som nøkkel (Keys)
og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden.


"""
# Land, hovedstad og antall innbyggere i millioner

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

print(data)