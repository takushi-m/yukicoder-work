# -*- coding: utf-8 -*-
n1 = int(input())
al = [int(x) for x in input().split()]
n2 = int(input())
bl = [int(x) for x in input().split()]

if n1==1:
    a1 = al[0]
    a2 = 1
else:
    a1 = al[0]
    a2 = al[1]
    for i in range(2,n1):
        a2 *= al[i]

if n2 == 1:
    b1 = bl[0]
    b2 = 1
else:
    b1 = bl[0]
    b2 = bl[1]
    for i in range(2,n2):
        if i%2==1:
            b2 *= bl[i]
        else:
            b1 *= bl[i]

c1 = a1*b2
c2 = a2*b1

def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

g = gcd(c1,c2)
c1 //= g
c2 //= g

print(c1,c2)
