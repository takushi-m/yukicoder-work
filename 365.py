# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))

if all([i+1==al[i] for i in range(n)]):
    print(0)
    exit()

cnt = 0
if al[0]==1:
    cnt += 1
c = al[0]
for i in range(1,n):
    if c<al[i]:
        c = al[i]
    else:
        cnt += 1
print(cnt)
