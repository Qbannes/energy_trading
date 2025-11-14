#!/usr/bin/env python3
# setzt Python 3.10 voraus!
lst = ['join', 2, 1]
match lst:
    case ['quit']:
        print('Programmende')
    case ['do', cmd]:
        print('Führe', cmd, 'aus.')
    case ['join', part1, part2] if part1 < part2:
        print(part1, 'ist kleiner als', part2)
    case ['join', part1, part2]:
        print('Füge', part1, 'und', part2, 'aneinander.')
    case ['join', *parts]:
         lst = [p for p in parts]
         print('Füge', lst, 'aneinander.')
    case _:
        print('Unbekanntes Kommando')
