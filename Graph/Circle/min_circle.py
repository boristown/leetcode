from Graph.ShortestPath.Dijkstra import dijkstraFull

inf = float("inf")

def min_circle(graph : dict):
    '''
    计算有向赋权图的最小环
    输入：
    graph:邻接表
    graph[p]返回p能直接访问的(结点,权值)list
    输出：
    最小的环路权值和
    '''
    #思路：
    # 枚举每条边(u,v)，长度为w
    # 删除边(u,v)，
    # 通过dijstra计算从v到u的最短路dis(v,u)
    # 环路长度等于dis(v,u) + w
    dis = dijkstraFull(graph)
    ans = inf
    for u in graph:
        for v,w in graph:
            ans = min(ans,w+dis[v,u])
    return ans