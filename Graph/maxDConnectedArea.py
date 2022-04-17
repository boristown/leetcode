def maxDConnectedArea(G):
    '''
    计算有向图的最大连通区域
    :param G:example [[set(),set([1,2])],[set(0),set()],[set(0),set()]]
    '''
    n=len(G)
    def dfs(i):
        if G[i][1]:
            for j in G[i][1]:
                if j not in vis:
                    vis.add(j)
                    dfs(j)
    ans=0
    for i in range(n):
        vis = {i}
        dfs(i)
        ans=max(ans,len(vis))
    return ans