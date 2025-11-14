#!/usr/bin/env python3
year = 2024

if year % 400 == 0:
    leapYear = True
elif year % 100 == 0:
    leapYear = False
elif year % 4 == 0:
    leapYear = True
else:
    leapYear = False
  
if leapYear:
    print(year, 'ist ein Schaltjahr.')
else:
    print(year, 'ist kein Schaltjahr.')