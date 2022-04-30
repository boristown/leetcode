#建图
from collections import *
def reverse_dg(DG):
    '''
    有向无权图(directed graph)转向
    '''
    gra2 = defaultdict(set)
    for a in DG:
        for b in DG[a]:
            gra2[b].add(a)
    return gra2

def reverse_adj(adj):
    '''
    有向赋权图（邻接表）转向
    '''
    adj2 = defaultdict(list)
    for u in adj:
        for v,w in adj[u]:
            adj2[v].append((u,w))
    return adj2