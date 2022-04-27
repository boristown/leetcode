#有向图的连通性判断
#by BorisTown 原创算法
#20220427
from collections import *
from Graph.BuidGraph import reverse_dg
from functools import *

class AnyToTarget:
    '''
    在有向图DG中，判断任意点到指定点的连通性
    '''
    def __init__(self,DG,target):
        '''
        DG：defaultdict(set)
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
        时间：O(1)
        '''
        return v in self.vis

class TargetToAny:
    '''
    在有向图DG中，判断指定点到任意点的连通性
    '''
    def __init__(self,DG,target):
        '''
        DG：defaultdict(set)
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
        时间：O(1)
        '''
        return v in self.vis

class AnyToAny:
    '''
    在有向图DG中，判断任意两点之间的连通性
    '''
    def __init__(self,DG):
        '''
        DG：defaultdict(set)
        '''
        self.DG = DG
    
    @cache
    def C(self,s,t):
        '''
        判断从s到t的连通性
        时间：O(E+V)
        '''
        if s == t:
            return True
        for s2 in self.DG[s]:
            if self.C(s2,t):
                return True
        return False