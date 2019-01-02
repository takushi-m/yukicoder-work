# -*- coding: utf-8 -*-

T = [0]*(10**6+1)
T[4] = 1
for i in range(5,len(T)):
    T[i] = (T[i-1]+T[i-2]+T[i-3]+T[i-4])%17

q = int(input())
ql = [int(input()) for _ in range(q)]

for q in ql:
    print(T[q])
