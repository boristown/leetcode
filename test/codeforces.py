from collections import *
INF = float("inf")
n = int(input())
L = list(map(int,input().split()))
def calculate(n,L):
    cnt = Counter()
    for i in range(n):
        cnt[L[i]%2] += 1
    d = cnt.most_common(1)[0][0]
    for i in range(n):
        if L[i]%2 != d:
            return i+1

print(calculate(n,L))