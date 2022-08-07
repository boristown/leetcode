from functools import *

def LongestPath(G):
    '''
    无向无环图中的最长路径
    '''
    ans = 0
    @cache
    def dp(i,j):
        '''
        从i,j出发的最长路径
        '''
        ans = 0
        for k in G[j]:
            if k!=i:
                ans = max(ans,1+dp(j,k))
        return ans
    
    for a in G:
        for b in G[a]:
            ans = max(ans,1+dp(a,b))
    return ans

def LongestPathIJ(G,i,j):
    '''
    在图G中，从i到j的最长路径
    '''
    