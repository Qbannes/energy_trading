#!/usr/bin/env python3
year = 2020
month = 2

if year % 400 == 0:
    leapYear = True
elif year % 100 == 0:
    leapYear = False
elif year % 4 == 0:
    leapYear = True
else:
    leapYear = False
  
if month in (1, 3, 5, 7, 8, 10, 12):
  days = 31
elif month in (4, 6, 9, 11):
  days = 30
elif month == 2:
  days = 29 if leapYear else 28
else:
  print('Ungültiges Monat!')
  days = 0

print('Das %d. Monat im Jahr %d hat %d Tage.' 
      % (month, year, days)) 
                
