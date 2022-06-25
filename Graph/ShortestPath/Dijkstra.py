#有向正权图的单源最短路算法
#Dijkstra 
#https://oi-wiki.org/graph/shortest-path/#dijkstra
from heapq import *
import heapq
import sys
from collections import *

def dijkstra(e,s):
    '''
    输入：
    e:邻接表
    s:起点
    返回：
    dis:从s到每个顶点的最短路长度
    '''
    dis = defaultdict(lambda:float("inf"))
    dis[s] = 0
    q = [(0,s)]
    vis = set()
    while q:
        _, u = heapq.heappop(q)
        if u in vis: continue
        vis.add(u)
        for v,w in e[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(q,(dis[v],v))
    return dis

def dijkstraF(e,s):
    '''
    输入：
    e:邻接函数表
    s:起点
    返回：
    dis:从s到每个顶点的最短路长度
    '''
    dis = defaultdict(lambda:float("inf"))
    dis[s] = 0
    q = [(0,s)]
    vis = set()
    while q:
        _, u = heapq.heappop(q)
        if u in vis: continue
        vis.add(u)
        for v,w in e(u):
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(q,(dis[v],v))
    return dis

def dijkstraFFull(graph):
    '''
    输入：
    e:邻接函数表
    返回：
    dis:任意两个顶点之间的最短路长度
    '''
    ans = {}
    for start in graph:
        dis = dijkstraF(graph,start)
        for end in dis:
            ans[start,end] = dis[end]
    return ans

def dijkstra_path(e,s,t):
    '''
    输入：
    e:邻接表
    s:起点
    t:终点
    返回：
    dis:从s到t的最短路径
    '''
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