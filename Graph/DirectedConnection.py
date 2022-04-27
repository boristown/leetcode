#有向图的连通性判断
#by BorisTown 原创算法
#20220427
from collections import *
import BuidGraph
from Graph.BuidGraph import reverse_dg

class AnyToTarget:
    '''
    判断任意点到指定点的连通性
    '''
    def __init__(self,DG,target):
        '''
        graph：defaultdict(set)
        '''
        #反向建图
        self.DG = reverse_dg(DG)
        #从target开始向外扩散并标记
        self.vis = set([target])
        self.dfs(target)

    def dfs(self,t):
        for v in self.DG[t]:
            if v not in self.vis:
                self.vis.add(v)
                self.dfs(v)

    def C(self,v):
        '''
        判断从v到target的连通性
        '''
        return v in self.vis

class TargetToAny:
    '''
    判断指定点到任意点的连通性
    '''
    def __init__(self,DG,target):
        '''
        graph：defaultdict(set)
        '''
        self.DG = DG
        #从target开始向外扩散并标记
        self.vis = set([target])
        self.dfs(target)

    def dfs(self,t):
        for v in self.DG[t]:
            if v not in self.vis:
                self.vis.add(v)
                self.dfs(v)

    def C(self,v):
        '''
        判断从v到target的连通性
        '''
        return v in self.vis

class AnyToAny:
    '''
    判断任意两点之间的连通性
    '''
    def __init__(self,graph):
        '''
        graph：defaultdict(set)
        '''
        pass
