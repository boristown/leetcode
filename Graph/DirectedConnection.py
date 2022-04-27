#有向图的连通性判断
#by BorisTown 原创算法
#20220427
from collections import *
import BuidGraph
from Graph.BuidGraph import reverse_dg

class AnyToTargetConnection:
    '''
    判断任意点到指定点的连通性
    '''
    def __init__(self,graph,target):
        '''
        graph：defaultdict(set)
        '''
        self.graph = graph
        #反向建图
        self.gra2 = reverse_dg(graph)
        #从target开始向外扩散并标记
        self.vis = set([target])
        self.dfs(target)

    def dfs(self,t):
        for v in self.gra2[t]:
            if v not in self.vis:
                self.vis.add(v)
                self.dfs(v)

    def C(self,v):
        return v in self.vis


class AnyToAnyConnection:
    '''
    判断任意两点之间的连通性
    '''
    def __init__(self,graph):
        '''
        graph：defaultdict(set)
        '''
        self.graph = graph
