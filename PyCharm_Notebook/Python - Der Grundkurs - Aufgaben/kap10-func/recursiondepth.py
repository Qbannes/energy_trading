#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10000)  # bleibt wirkungslos

# diese Funktion ist absichtlich fehlerhaft formuliert,
# so dass sie eine endlose Rekursion auslöst
def f(n):
    return 1 + f(n)
    
f(2)  # RecursionError: maximum recursion depth exceeded
    