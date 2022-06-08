# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 23:22:06 2022

@author: Michał
"""

import random

def pesel():
#rok - dwie cyfry
   rok = float(input("Podaj rok: "))

#miesiac - dwie cyfry
   if rok <= 1999:
      miesiac = float(input("Podaj miesiąc: "))

   elif rok > 1999:
      miesiac = float(input("Podaj miesiąc: ")) + 20 

#dzien - dwie cyfry
   dzien = float(input("Podaj dzień urodzenia: "))

#trzycyfrowy numer serii
   nr_serii = random.randint(100,999)
   nr_serii = str(nr_serii)
   plec = float(input("Wpisz '1' jeżeli to mężczyzna lub '2' dla kobiety: "))
   
   if plec==1:
       plec = ((random.randint(1,5) * 2)-1)
   else:
       plec = (random.randint(0,4) * 2)
       

   r = '%02d' % (rok % 100)
   m = '%02d' % miesiac
   dd = '%02d' % dzien

   temp = [0,0,0,0,0,0,0,0,0,0]
   temp[0] = int(r[0])
   temp[1] = int(r[1])
   temp[2] = int(m[0])
   temp[3] = int(m[1])
   temp[4] = int(dd[0])
   temp[5] = int(dd[1])
   temp[6] = int(nr_serii[0])
   temp[7] = int(nr_serii[1])
   temp[8] = int(nr_serii[2])
   temp[9] = int(plec)

   algorytm_kontrolny = temp[0] + 3 * temp[1] + 7 * temp[2] + 9 * temp[3] + temp[4] + 3 * temp[5] + 7 * temp[6] + 9 * temp[7] + temp[8] + 3 * temp[9]

# kontrolna - jedna cyfra
   if algorytm_kontrolny % 10 == 0:
      kontrolna = 0
   else:
      kontrolna = 10 - (algorytm_kontrolny % 10)

   print(r, end='')
   print(m, end='')
   print(dd, end='')
   print(nr_serii, end='')
   print(plec, end='')
   print(kontrolna)


liczba_peseli = int(input("Podaj ile Peseli chcesz wygerować: "))

for i in range (liczba_peseli):
    pesel()
