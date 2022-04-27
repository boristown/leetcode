#有向正权图的单源最短路算法
#Dijkstra 
#https://oi-wiki.org/graph/shortest-path/#dijkstra
from heapq import *
from collections import *

def dijkstra(graph,s):
    '''
    在有向正权图中：从s出发到所有节点的最短路长度
    graph:defaultdict(dict)
    '''
    Q = [(0,s)]
    ans = defaultdict(lambda:float("inf"))
    ans[s] = 0
    while Q:
        _, node = heappop(Q)
        for node2 in graph[node]:
            dis = ans[node] + graph[node][node2]
            if ans[node2] > dis:
                ans[node2] = dis
                heappush(Q,(dis,node2))
    return ans