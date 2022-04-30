#有向正权图的单源最短路算法
#Dijkstra 
#https://oi-wiki.org/graph/shortest-path/#dijkstra
from heapq import *
import heapq
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