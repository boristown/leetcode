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
        '''
        合并
        '''
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
        '''
        连通性
        '''
        x, y = self.findset(x), self.findset(y)
        return x == y
    
    def isolate(self, x: int) -> None:
        '''
        孤立
        '''
        if self.parent[x] != x:
            self.parent[x] = x
            self.size[x] = 1
            self.setCount += 1