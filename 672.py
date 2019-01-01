# -*- coding: utf-8 -*-
s = list(input())
n = len(s)

d = {0:-1}
cnt = 0
res = 0
for i in range(n):
    if s[i]=="A":
        cnt += 1
    else:
        cnt -= 1

    if cnt in d:
        res = max(res, i-d[cnt])
    else:
        d[cnt] = i

print(res)
