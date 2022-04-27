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