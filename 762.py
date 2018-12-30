# -*- coding: utf-8 -*-
n,m = map(int, input().split())
s = list(input())
edge = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    if (s[u]=="P" and s[v]=="D" or
        s[u]=="D" and s[v]=="C" or
        s[u]=="C" and s[v]=="A"
    ):
        edge[u].append(v)

    if (s[v]=="P" and s[u]=="D" or
        s[v]=="D" and s[u]=="C" or
        s[v]=="C" and s[u]=="A"
    ):
        edge[v].append(u)

dp = [[0 for _ in range(n)] for _ in range(4)]

for i in range(n):
    if s[i]=="P":
        dp[0][i] = 1

for u in range(n):
    for v in edge[u]:
        if s[v]=="D":
            dp[1][v] += dp[0][u]

for u in range(n):
    for v in edge[u]:
        if s[v]=="C":
            dp[2][v] += dp[1][u]

for u in range(n):
    for v in edge[u]:
        if s[v]=="A":
            dp[3][v] += dp[2][u]

res = sum(dp[3])%(10**9 + 7)
print(res)
