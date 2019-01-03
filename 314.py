# -*- coding: utf-8 -*-
n = int(input())
MOD = 10**9 + 7

k = 1
kk = 0
p = 0
for _ in range(n-1):
    k,kk,p = p,k,(k+kk)%MOD

print((k+kk+p)%MOD)
