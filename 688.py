# -*- coding: utf-8 -*-
k = int(input())

if k==0:
    print("1")
    print("1")
    exit()

def calc(n,m):
    # k = n*(n-1)//2 * 2**m
    if k%(n*(n-1)//2)==0:
        k2 = k//(n*(n-1)//2)
        if m==0:
            return k2==1
        for i in range(m):
            if k2%2==0:
                k2 //= 2
            else:
                return False
        return k2==1
    else:
        return False

for n in range(2,30+1):
    for m in range(0,30-n+1):
        if calc(n,m):
            res = ["1"]*(n) + ["0"]*m
            print(n+m)
            print(" ".join(res))
            exit()
