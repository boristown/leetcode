#k短路
#https://oi-wiki.org/graph/kth-path/

from Graph.BuidGraph import reverse_adj
from Graph.ShortestPath.Dijkstra import dijkstra
from Graph.ShortestPath.astar import astar_k

def kthPath(adj,s,t,k):
    '''
    输入：
    adj:正权图(邻接表)
    s:起点
    t:终点
    k:第k短路
    返回：
    ans:从s到t的第k短路
    '''
    adj2 = reverse_adj(adj)
    dis = dijkstra(adj2,t)
    ans = astar_k(adj,s,t,k,lambda i:dis[i])
    return ans