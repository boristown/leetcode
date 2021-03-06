from collections import *
from itertools import *
import itertools
import numpy as np
import heapq

from sortedcontainers import SortedList
from constants import *
from Graph.GraphBase import *
from Graph.UnionFind import *
from PQ import *
from String.Trie import *
from Others.TreeCheck import *
import math
import bisect
from functools import *
from segtree.SegSumTree import *

def strhash(s,mod):
    '''
    字符串hash(仅小写字母)
    #a->1
    #z->26
    #aa->27
    #za->52
    适用场景：字符串匹配
    '''
    s = [ord(c)-ord('a')+1 for c in s]
    b = 1
    ans = 0
    for v in s:
        ans = (ans + v * b)%mod
        b*=26
    return ans

def any2dec(origin, x):
    '''
    m: int 
	origin：str
	return: int
    任意进制的数转换为10机制
    直接利用int的自带功能
    适用场景：进制转换
    '''
    return int(str(origin), base = x) # origin必须是字符串

def dec2any(n,x):
    '''
    10进制转N进制
    n为待转换的十进制数，x为机制，取值为2-16
    适用场景：进制转换
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


def prefix2D(matrix):
    '''
    计算二维前缀和
    适用场景：二维前缀和
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
    适用场景：整数翻转
    """
    ans = 0
    while num:
        ans = 10 * ans + num % 10
        num /= 10
    return ans

def LIS1(self, nums, strictMode = True) -> int:
    '''
    O(n^2)
    最长上升子序列
    nums:数字序列
    strictMode：True上升序列，False非降序列,默认True
    适用场景：最长上升子序列
    '''
    if not nums:
        return 0
    dp = []
    if strictMode:
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
    else:
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] >= nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def LIS2(self, nums, strictMode = True) -> int:
    '''
    O(n * log n)
    最长上升子序列
    nums:数字序列
    strictMode：True上升序列，False非降序列,默认True
    适用场景：最长上升子序列
    '''
    dp = []
    if strictMode:
        for m in nums:
            p=bisect.bisect_left(dp,m)
            if p==len(dp): dp.append(m)
            else: dp[p]=m
    else:
        for m in nums:
            p=bisect.bisect_right(dp,m)
            if p==len(dp): dp.append(m)
            else: dp[p]=m
    return len(dp)

def LCS(text1: str, text2: str) -> int:
    """
    最长公共子序列（双串）
    适用场景：最长公共子序列
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
    适用场景：直方图的最大矩形面积
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
    '''
    适用场景：双向链表
    '''
    def __init__(self, value=0):
        self.value = value
        self.prev = None
        self.next = None

class DLinkedList:
    '''
    适用场景：双向链表
    '''
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
    '''
    适用场景：链表
    '''
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
    '''
    适用场景：字母状态压缩
    '''
    @staticmethod
    def word2bin(w):
        b=0
        for c in w:
            i=ord(c)-ord("a")
            b |= 1<<i
        return b

class bfs_utils:
    '''
    适用场景：bfs
    '''
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
    '''
    适用场景：bfs
    '''
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

class CourseScheduler:
    '''
    适用场景：课程规划
    '''
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

def gcd(a,b):
    '''
    求a与b的最大公因数gcd
    适用场景：最大公因数
    '''
    if b!=0:
        return gcd(b,a%b)
    else:
        return a

def get_factors(a):
    '''
    计算a的所有因子
    适用场景：因子分解
    '''
    ans = set()
    for i in range(1,int(math.sqrt(a))+1):
        if not a%i:
            ans.add(i)
            ans.add(a//i)
    return ans

g_factor_idx = 0

@cache
def primes_factors(x):
    '''
    质因子分解
    适用场景：因子分解
    '''
    ans = Counter()
    if x<2: return ans
    if x in pset:
        ans[x] +=1
        return ans
    np = len(primes)
    global g_factor_idx
    while x>1 and g_factor_idx<np:
        p = primes[g_factor_idx]
        if x % p == 0:
            ans[p]+=1
            x //= p
            return ans + primes_factors(x)
        else:
            g_factor_idx+=1

