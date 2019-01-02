# -*- coding: utf-8 -*-
n,lb,rb = map(int, input().split())
xl = [list(map(int, input().split())) for _ in range(n)]

def check(x):
    hit = -1
    for i in range(n):
        if xl[i][0]<=x<=xl[i][2]:
            if hit==-1:
                hit = i
            else:
                if xl[i][3]>xl[hit][3]:
                    hit = i
    return hit

hitList = [0]*n
x = lb
while x<=rb:
    hitIdx = check(x)
    if hitIdx>-1:
        hitList[hitIdx] = 1

    x += 1

for h in hitList:
    print(h)
