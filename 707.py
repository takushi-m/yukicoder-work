# -*- coding: utf-8 -*-
from math import sqrt
h,w = map(int, input().split())
p = [list(input()) for _ in range(h)]

def calc(x,y):
    res = 0
    for hi in range(h):
        for wi in range(w):
            if p[hi][wi]=="1":
                res += sqrt((x-wi-1)**2 + (y-hi-1)**2)
    return res

res = 10**9
for hi in range(h):
    res = min(res, calc(0,hi+1))
    res = min(res, calc(w+1,hi+1))
for wi in range(w):
    res = min(res, calc(wi+1,0))
    res = min(res, calc(wi+1,h+1))

print(res)
