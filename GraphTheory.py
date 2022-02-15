import itertools
from collections import *
from UnionFind import *

class GraphTheory:
    '''
    图论工具类
    '''
    @staticmethod
    def matrix2graph(grid) -> dict:
        '''
        邻接矩阵转无向图
        '''
        graph = {}
        n = len(grid)
        for i in range(n-1):
            for j in range(i+1,n):
                if grid[i][j]:
                    if i not in graph:
                        graph[i] = set()
                    if j not in graph:
                        graph[j] = set()
                    graph[i].add(j)
                    graph[j].add(i)
        return graph

    @staticmethod
    def maze2graph(grid) -> dict:
        '''
        二维迷宫转无向图
        param grid:二维矩阵，1是有效区域，0是无效区域
        时间：O(m*n)
        空间：O(m*n)
        '''
        m=len(grid)
        n=len(grid[0])
        num=m*n
        nab = [(0,1),(0,-1),(1,0),(-1,0)]
        graph = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    idx = i*n+j
                    graph[idx] = set()
                    for a,b in nab:
                        i2,j2=i+a,j+b
                        if 0<=i2<m and 0<=j2<n and grid[i2][j2]:
                            idx2 = i2*n+j2
                            graph[idx].add(idx2)
        return graph

    @staticmethod
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

    @staticmethod
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
    
    @staticmethod
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
        
class TopologicalSortor:
    '''
    拓扑排序器
    '''
    def __init__(self,vertices): 
        self.graph = defaultdict(set)
        self.V = vertices
    
    def detectCircle(self,u):
        self.detectedNode.add(u)
        for v in self.graph[u]:
            if v not in self.pathNode:
                self.pathNode.add(v)
                self.detectCircle(v)
                self.pathNode.remove(v)
                if self.findCircle:
                    return
            else:
                self.findCircle = True
                return

    def addEdge(self,u,v):
        '''
        添加路径
        '''
        if v not in self.graph[u]:
            self.graph[u].add(v)
    
    def hasCircle(self):
        '''
        环路检测器
        '''
        self.pathNode = set()
        self.detectedNode = set()
        for i in range(self.V):
            if i not in self.detectedNode:
                self.findCircle = False
                self.pathNode.add(i)
                self.detectCircle(i)
                self.pathNode.remove(i)
                if self.findCircle: return True
        return False
  
    def topologicalSortUtil(self,v,visited,stack):
        visited[v] = True
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
        stack.insert(0,v)
  
    def topologicalSort(self):
        '''
        拓扑排序
        '''
        visited = [False]*self.V 
        stack =[] 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
        self.stack = stack
        return stack
    
    def is_Hamiltonian_path(self):
        '''
        拓扑排序的唯一性判断（哈密顿路径）
        '''
        for i in range(self.V - 1):
            a,b = self.stack[i],self.stack[i+1]
            if b not in self.graph[a]:
                return False
        return True
        
def optimize_assignment(n,cost_func,maximize=False):
    '''
    二分图的最优代价分配：匈牙利算法
    n:元素数量
    cost_func:代价函数，以(i,j)为入参，返回个代价值
    maximize:寻找最大(True)/最小(False)代价
    返回值:最优代价，分配方案
    '''
    from scipy.optimize import linear_sum_assignment
    import numpy as np
    cost = np.zeros((n, n))
    for i,j in itertools.product(range(n),range(n)):
        cost[i,j] = cost_func(i,j)
    row,col = linear_sum_assignment(cost,maximize=maximize)
    return int(cost[row,col].sum()),col

def TSP(graph):
    '''
    旅行商问题:状压DP
    在一个图中，从某个点出发将所有点恰好遍历一遍，使得最后路过的路径的总权值最大
    graph：有向带权图graph[i][j]表示从i到j的权值
    返回值：最大权值，最优路径
    '''
    N=len(graph)
    # dp[mask][i] = most overlap with mask, ending with ith element
    dp = [[0] * N for _ in range(1<<N)]
    parent = [[None] * N for _ in range(1<<N)]
    for mask in range(1, 1 << N):
        for bit in range(N):
            if (mask >> bit) & 1:
                # Let's try to find dp[mask][bit].  Previously, we had
                # a collection of items represented by pmask.
                pmask = mask ^ (1 << bit)
                if pmask == 0: continue
                for i in range(N):
                    if (pmask >> i) & 1:
                        # For each bit i in pmask, calculate the value
                        # if we ended with word i, then added word 'bit'.
                        value = dp[pmask][i] + graph[i][bit]
                        if value > dp[mask][bit]:
                            dp[mask][bit] = value
                            parent[mask][bit] = i

    # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
    # Reconstruct answer:

    # Follow parents down backwards path that retains maximum overlap
    ans = []
    mask = (1<<N) - 1
    i = max(range(N), key = dp[-1].__getitem__)
    max_weight = dp[-1][i]

    while i is not None:
        ans.append(i)
        mask, i = mask ^ (1<<i), parent[mask][i]

    # Reverse path to get forwards direction; add all remaining words
    ans = ans[::-1]
    seen = [False] * N
    for x in ans:
        seen[x] = True
    ans.extend([i for i in range(N) if not seen[i]])
    return max_weight,ans
