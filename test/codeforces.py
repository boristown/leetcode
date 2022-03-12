from collections import *
INF = float("inf")

def process(n,m,M):
    return 0

n,m = map(int,input().split())
M = []
for i in range(n):
    L = list(map(int,input().split()))
    M.append(L)
print(process(n,m,M))