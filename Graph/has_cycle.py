from Graph.UnionFind import *

def has_cycle(G):
    '''
    判断无向图是否有环
    :param G: example [set([1,2]),set([3]), set([])]
    :return:True有环，False无环
    '''
    n=len(G)
    UF=UnionFind(n)
    for i in range(n):
        for j in G[i]:
            #如果连接i,j两点之前，i,j已经连通，则说明存在环
            if UF.connected(i,j):
                return True
            UF.unite(i,j)
    return False