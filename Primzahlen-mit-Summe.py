#!/usr/bin/python3

import math

start = 300
sum = 0

print(start, end='')

for i in range(start,1,-1):
  prime=True

  for j in range(2,math.isqrt(i)+1):
    if (i%j==0):
      prime = False
 
  if prime:
    print( ' |', i, end='')
    sum = sum + i

print(' |')

print('Summe der Primzahlen bis', start, ':', sum)

