from collections import defaultdict
import heapq

def astar_k(adj,s,t,k,H):
    '''
    输入：
    adj:正权图(邻接表)
    s:起点
    t:终点
    k:第k短路
    H:到目标的距离评估
    返回：
    ans:从s到t的第k短路
    '''
    dis = defaultdict(lambda:float("inf"))
    dis[s] = 0
    q = [(0+H(s),s)]
    vis = set()
    while q:
        _, u = heapq.heappop(q)
        if u in vis: continue
        vis.add(u)
        for v,w in adj[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(q,(dis[v],v))
    return dis