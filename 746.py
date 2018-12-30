# -*- coding: utf-8 -*-
from decimal import Decimal,getcontext
getcontext().prec = 10**5
n = int(input())
cnt = (10**n)//(7)
if cnt==0:
    print(0)
else:
    print(Decimal(cnt)/(Decimal(10)**Decimal(n)))
