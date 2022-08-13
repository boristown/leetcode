#begin of codeforces template
# (don't delete):
#  
# from collections import *
# from heapq import *
# import bisect
#
#t = int(input()) #input number of test cases
#for _ in range(t): #iter for test cases
#    n = int(input()) #input int
#    n,m = map(int,input().split()) #input tuple
#    A = list(map(int,input().split())) #input list
#    s = input() #input string
#    ans = solve(s,L) #solve
#    print(ans) #print single answer
#    print(" ".join(map(str,ans))) #print int array
#
#end of codeforces template

from collections import *
from itertools import *

inf = float("inf")

# 并查集模板
class UnionFind:
    '''
    适用范围：连通性检测
    '''
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n
    
    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]
    
    def un(self, x: int, y: int) -> bool:
        '''
        unite合并
        '''
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def co(self, x: int, y: int) -> bool:
        '''
        connected连通性
        '''
        x, y = self.findset(x), self.findset(y)
        return x == y

CO = set()
V = [(0,0)]
N,M,E = map(int,input().split()) #input tuple
for i in range(E): #iter for test cases
    u,v = map(int,input().split()) #input tuple
    CO.add((u-1,v-1))
    V.append((u-1,v-1))
sup = N+M
tot = sup+1
UF = UnionFind(tot)
for i in range(N,M+N):
    UF.un(i,sup)
Q = int(input()) #input int
QL = []
for _ in range(Q): #iter for test cases
    x = int(input()) #input int
    QL.append(V[x])
    CO.remove(V[x])
for u,v in CO:
    UF.un(u,v)

ans = []
for u,v in QL[::-1]:
    ans.append(UF.size[UF.findset(sup)]-M-1)
    UF.un(u,v)

for i in range(Q-1,-1,-1):
    print(ans[i])