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
#    L = list(map(int,input().split())) #input list
#    s = input() #input string
#    ans = solve(s,L) #solve
#    print(ans)
#
#end of codeforces template 

from collections import *
import heapq

def dijkstra_path(e,s,t):
    dis = defaultdict(lambda:float("inf"))
    dis[s] = 0
    q = [(0,s)]
    vis = set()
    last = {} #last node
    while q:
        _, u = heapq.heappop(q)
        if u in vis: continue
        vis.add(u)
        for v,w in e[u]:
            if dis[v] > dis[u] + w:
                last[v] = u
                dis[v] = dis[u] + w
                heapq.heappush(q,(dis[v],v))
    if t not in last:
        return []
    ans = [t]
    while t in last:
        ans.append(last[t])
        t = last[t]
    return ans[::-1]

n,m = map(int,input().split()) #input tuple
G = defaultdict(list)
for _ in range(m): #iter for test cases
    a,b,w = map(int,input().split()) #input tuple
    if a!=b:
        G[a].append((b,w))
        G[b].append((a,w))
#print(G)
ans = dijkstra_path(G,1,n)
if not ans: 
    print(-1)
else:
    print(" ".join(map(str,ans)))