# -*- coding: utf-8 -*-
n,x = map(int, input().split())
al = [int(x) for x in input().split()]
al.sort()


def lower_bound(al, key):
    def isOk(a):
        return a>=key
    ng = -1
    ok = len(al)
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if isOk(al[mid]):
            ok = mid
        else:
            ng = mid
    return ok

def upper_bound(al, key):
    def isOk(a):
        return a>key
    ng = -1
    ok = len(al)
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if isOk(al[mid]):
            ok = mid
        else:
            ng = mid
    return ok

cnt = 0
for a in al:
    l = lower_bound(al, x-a)
    u = upper_bound(al, x-a)
    if u>l>=0:
        cnt += u-l

print(cnt)
