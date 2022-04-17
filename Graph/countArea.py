def countArea(graph) -> int:
    '''
    统计图中的独立区域数
    :param graph:无向图 example: {0:set([1,2]),1:set([0,2),2:set([0,1])}
    时间：O(m*n)
    空间：O(m*n)
    '''
    vis,ans=set(),0
    def dfs(i):
        vis.add(i)
        for j in graph[i]:
            if j not in vis:
                dfs(j)
    #枚举每个节点
    for i in graph:
        #节点未访问，区域+1
        if i not in vis:
            ans+=1
            dfs(i)
    return ans