from collections import *
from itertools import *
import itertools
import numpy as np
import heapq
from matrix import *
from constants import *
from graph import *
from UnionFind import *
from PQ import *
from Trie import *

def A(n,m):
    '''
    从n个元素中选择m个排列数
    '''
    ans = 0
    for i in range(n,n-m,-1):
        ans *= i
    return ans

def C(n,m):
    '''
    从n个元素中选择m个组合数
    '''
    ans = A(n,m)
    x = 1
    for i in range(1,m+1):
        x *= i
    return ans // x

def any2dec(origin, x):
    '''
    m: int 
	origin：str
	return: int
    任意进制的数转换为10机制
    直接利用int的自带功能
    '''
    return int(str(origin), base = x) # origin必须是字符串

def dec2any(n,x):
    '''
    10进制转N进制
    n为待转换的十进制数，x为机制，取值为2-16
    '''
    a=['0','1','2','3','4','5','6','7','8','9','A','b','C','D','E','F']
    b=[]
    while True:
        s=n//x  # 商
        y=n%x  # 余数
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    x=""
    for i in b:
        x+=a[i]
    return x

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

def int_reverse(num: int)->int:
    """
    整数翻转
    """
    ans = 0
    while num:
        ans = 10 * ans + num % 10
        num /= 10
    return ans

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

class DLinkedNode:
    def __init__(self, value=0):
        self.value = value
        self.prev = None
        self.next = None

class DLinkedList:

    def __init__(self):
        self.cache = dict()
        # 使用伪头部和伪尾部节点    
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def Node2List(head):
        L,p = [],head
        while p:
            L.append(p.val)
            p = p.next
        return L
    
    @staticmethod
    def List2Node(L):
        n=len(L)
        N = []
        for l in L:
            N.append(ListNode(l,None))
        for i,node in enumerate(N[:n-1]):
            node.next = N[i+1]
        return N[0]

class StateCompression:
    @staticmethod
    def word2bin(w):
        b=0
        for c in w:
            i=ord(c)-ord("a")
            b |= 1<<i
        return b

class bfs_utils:
    @staticmethod
    def nxt(x):
        if x%2==0:
            yield x//2
        else:
            yield x+1
            yield x-1
    @staticmethod
    def bfs(n):
        if n==1: return 0
        Q = deque([(0,n)])
        seen = set([n])
        while Q:
            step,x=Q.popleft()
            step1 = step + 1
            for y in bfs_utils.nxt(x):
                if y not in seen:
                    if y == 1:
                        return step1
                    seen.add(y)
                    Q.append((step1,y))
        return -1

class bfs_utils_2D:
    def __init__(self,grid,sx,sy,tx,ty):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.sx = sx
        self.sy = sy
        self.tx = tx
        self.ty = ty

    def nxt(self,x,y):
        for a,b in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = x+a,y+b
            if 0<=nx<self.m and 0<=ny<self.n and self.grid[nx][ny]:
                yield nx,ny

    def bfs(self):
        if (self.sx,self.sy) == (self.tx,self.ty): return 0
        Q = deque([(0,self.sx,self.sy)])
        seen = set([(self.sx,self.sy)])
        while Q:
            step,i,j=Q.popleft()
            step1 = step + 1
            for a,b in self.nxt(i,j):
                if (a,b) not in seen:
                    if (a,b) == (self.tx,self.ty):
                        return step1
                    seen.add((a,b))
                    Q.append((step1,a,b))
        return -1

class BinarySearch:
    '''
    二分查找工具包
    '''
    @staticmethod
    def bisect_right(l,r,func):
        '''
        右侧查找
        '''
        while l<r:
            mid=(l+r)//2
            if func(mid):
                r=mid
            else:
                l=mid+1
        return r

    @staticmethod
    def bisect_left(l,r,func):
        '''
        左侧查找
        '''
        while l<r:
            mid=(l+r)//2+1
            if func(mid):
                l=mid
            else:
                r=mid-1
        return l

class CourseScheduler:
    @staticmethod
    def schedule_by_duration_lastDay(courses) -> list:
        '''
        :这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，
        其中 courses[i] = [durationi, lastDayi] 表示第 i 门课将会 持续 上 durationi 天课，
        并且必须在不晚于 lastDayi 的时候完成。
        你的学期从第 1 天开始。
        且不能同时修读两门及两门以上的课程。
        返回你可以修读最多课程的方案。
        :param courses: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
        '''
        courses = [[i,course[0],course[1]] for i,course in enumerate(courses)]
        courses.sort(key=lambda c: c[2])

        q = list()
        # 优先队列中所有课程的总时间
        total = 0

        for idx, ti, di in courses:
            if total + ti <= di:
                total += ti
                # Python 默认是小根堆
                heapq.heappush(q, (-ti,di,idx))
            elif q and -q[0][0] > ti:
                total -= -q[0][0] - ti
                heapq.heappop(q)
                heapq.heappush(q, (-ti,di,idx))

        q.sort(key=lambda c:c[1])
        return [a[2] for a in q]

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
