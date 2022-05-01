from collections import *
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
    if s == t: 
        return 0 if k == 1 else -1
    q = [(0+H(s),0,s)]
    cnt = Counter() #记录节点入堆的次数
    cnt[s] += 1
    cnt2 = Counter() #记录访问到节点的次数
    while q:
        _, dis, u = heapq.heappop(q)
        for v,w in adj[u]:
            cnt2[v]+=1
            dis2 = dis+w
            if v == t:
                if cnt2[v] == k:
                    return dis2
            if cnt[u] < k:
                cnt[u] += 1
                heapq.heappush(q,(dis2+H[v],dis2,v))
    return -1