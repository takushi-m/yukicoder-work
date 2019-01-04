# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))

if all([i+1==al[i] for i in range(n)]):
    print(0)
    exit()

cnt = 0
maxN = n
for i in range(n-1,-1,-1):
    # print(i,maxN)
    if al[i]!=maxN:
        cnt += 1
    else:
        maxN -= 1


print(cnt)
