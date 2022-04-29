#有向负权图的单源最短路算法
#SPFA
#https://oi-wiki.org/graph/shortest-path/#bellman-ford
from curses.ascii import NL
from heapq import *
from collections import *

def SPFA(graph,s):
    '''
    在有向负权图中：从s出发到所有节点的最短路长度
    graph:defaultdict(dict)
    '''
    n = len(graph)
    Q = deque([(0,s)])
    ans = defaultdict(lambda:float("inf"))
    ans[s] = 0
    cnt = Counter()
    A = set([s])
    cnt[s]+=1
    while Q:
        _, node = Q.popleft()
        A.remove(node)
        for node2 in graph[node]:
            dis = ans[node] + graph[node][node2]
            if ans[node2] > dis:
                ans[node2] = dis
                if node2 not in A:
                    A.add(node2)
                    Q.append((dis,node2))
                    cnt[node2]+=1
                    if cnt[node2] > n:
                        return [] #存在负环
    return ans