# -*- coding: utf-8 -*-
n = int(input()) + 1
al = [int(input()) for _ in range(n)]
bl = [int(input()) for _ in range(n)]

accb = [0]*n
accb[0] = bl[0]
for i in range(1,n):
    accb[i] = accb[i-1]+bl[i]

res = 0
for i in range(n):
    res += al[i]*accb[n-i-1]

print(res%(10**9+7))
