from collections import defaultdict

Inf = float("inf")
# 并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n
    
    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None

class TopologicalSortor:
    '''
    拓扑排序器
    '''
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def topologicalSortUtil(self,v,visited,stack): 
  
        visited[v] = True
  
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        stack.insert(0,v) 
  
    def topologicalSort(self): 
        visited = [False]*self.V 
        stack =[] 
  
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        return stack

def prefix2D(matrix):
    '''
    二维前缀和
    '''
    if not matrix: return matrix
    height=len(matrix)
    width=len(matrix[0])
    prefix=[[0] * (width+1) for _ in range(height+1)]
    for i in range(1,height+1):
        for j in range(1,width+1):
            prefix[i][j]=prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+matrix[i-1][j-1]
    return prefix

def LCS(text1: str, text2: str) -> int:
    """
    最长公共子序列
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

def largestRectangleArea(heights) -> int:
    '''
    剑指 Offer II 039. 直方图最大矩形面积
    '''
    stack=[(-1,-1)]
    heights.append(0)
    ans=0
    for i,h in enumerate(heights):
        while stack[-1][1]>h:
            _,oh = stack.pop()
            s=(i-stack[-1][0]-1)*oh
            ans=max(ans,s)
        stack.append((i,h))
    return ans