#!/usr/bin/env python3
day = 3   # 1 = Montag, ..., 7 = Sonntag
if day in (1, 2, 3, 4, 5):
    print('arbeiten ...')
elif day in (6, 7):
    print('wochenende')
else:
    print('ungültig')

if day == 1:
  s = 'Montag'
elif day == 2:            
  s = 'Dienstag'
elif day == 3:            
  s = 'Mittwoch'
elif day == 4:            
  s = 'Donnerstag'
elif day == 5:            
  s = 'Freitag'
elif day == 6:            
  s = 'Samstag'
elif day == 7:            
  s = 'Sonntag'
else:
  s = 'ungültig'  
print("Wochentag:", s)

alldays = { 1: 'Montag', 2: 'Dienstag', 3: 'Mittwoch', 
  4: 'Donnerstag', 5: 'Freitag', 6: 'Samstag', 
  7: 'Sonntag'}

if day in alldays:
  s = alldays[day]
else:
  s = 'ungültig'
print("Wochentag:", s)  