# -*- coding: utf-8 -*-
n = int(input())
if n==1:
    print("n")
    exit()

c = "qwertyuiopasdfghjk"

def next(wl):
    wl[0] += 1
    for i in range(len(wl)):
        if wl[i]>17:
            wl[i] = 0
            wl[i+1] += 1

def conv(wl):
    w = [c[i] for i in wl]
    return "".join(w)

w = [0]*18
for i in range(n-1):
    next(w)
    print("a"+conv(w)+"a")
print("an")
