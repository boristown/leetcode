#k短路
#https://oi-wiki.org/graph/kth-path/

from Graph.BuidGraph import reverse_dg


def kthPath(adj,s,t,k):
    '''
    输入：
    adj:正权图(邻接表)
    s:起点
    t:终点
    k:第k短路
    返回：
    dis:从s到t的第k短路
    '''
    adj = reverse_dg(adj)