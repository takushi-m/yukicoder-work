# -*- coding: utf-8 -*-
from copy import deepcopy

h,w = map(int, input().split())
s = [input() for _ in range(h)]

def check(dh,dw):
    s2 = [[1 if s[hi][wi]=="#" else 0 for wi in range(w)] for hi in range(h)]
    for hi in range(h):
        for wi in range(w):
            if s2[hi][wi]==1:
                if h>hi+dh>=0 and w>wi+dw>=0:
                    if s2[hi+dh][wi+dw]==1:
                        s2[hi][wi] = 2
                        s2[hi+dh][wi+dw] = 3
                    else:
                        return False
                else:
                    return False
    return True

black = []
for hi in range(h):
    for wi in range(w):
        if s[hi][wi]=="#":
            black.append((hi,wi))
if len(black)>0:
    hi,wi = black[0]
    for i in range(1,len(black)):
        hi2,wi2 = black[i]
        if check(hi2-hi, wi2-wi):
            print("YES")
            exit()
print("NO")
