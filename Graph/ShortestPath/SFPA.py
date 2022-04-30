#有向负权图的单源最短路算法
#SPFA
#https://oi-wiki.org/graph/shortest-path/#bellman-ford
from heapq import *
from collections import *

def SPFA(adj,s):
    '''
    输入：
    adj:邻接表
    s:起点
    返回：
    dis:从s到每个顶点的最短路长度
    '''
    n = len(adj)
    Q = deque([(0,s)])
    dis = defaultdict(lambda:float("inf"))
    dis[s] = 0
    cnt = Counter()
    A = set([s])
    cnt[s]+=1
    while Q:
        _, u = Q.popleft()
        A.remove(u)
        for v,w in adj[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                if v not in A:
                    A.add(v)
                    Q.append((dis[v],v))
                    cnt[v]+=1
                    if cnt[v] > n:
                        return [] #存在负环
    return dict(dis)