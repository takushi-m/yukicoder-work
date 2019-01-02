# -*- coding: utf-8 -*-
from math import log10,floor
from decimal import Decimal

s = input()

k = len(s)-1
x = s[:3]

if int(x[2])>4:
    x = int(x[:2])+1
else:
    x = int(x[:2])

x /= 10

if x>=10.0:
    x /= 10
    k += 1

print("{}*10^{}".format(x,k))
