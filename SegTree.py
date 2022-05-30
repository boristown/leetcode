from functools import reduce

class SegTree:
    '''
    通用线段树 by AK自动机
    支持增量更新，覆盖更新，序列更新，任意RMQ操作
    基于二叉树实现
    初始化：O(1)
    增量更新或覆盖更新的单次操作复杂度：O(log k)
    序列更新的单次复杂度：O(n)
    https://github.com/boristown/leetcode/blob/main/SegTree.py
    '''
    def __init__(self, f1, f2, l, r, v = 0):
        '''
        初始化线段树[left,right)
        f1,f2示例：
        线段和:
        f1=lambda a,b:a+b 
        f2=lambda a,n:a*n
        线段最大值:
        f1=lambda a,b:max(a,b)
        f2=lambda a,n:a
        线段最小值:
        f1=lambda a,b:min(a,b)
        f2=lambda a,n:a
        '''
        self.ans = '?'
        self.f1 = f1
        self.f2 = f2
        self.l = l #left
        self.r = r #right
        self.v = v #init value
        self.lazy_tag = 0 #Lazy tag
        self.left = None #SubTree(left,bottom)
        self.right = None #SubTree(right,bottom)
    
    @property
    def mid_h(self):
        return (self.l + self.r) // 2

    def create_subtrees(self):
        midh = self.mid_h
        if not self.left and midh > self.l:
            self.left = SegTree(self.f1, self.f2, self.l, midh)
        if not self.right:
            self.right = SegTree(self.f1, self.f2, midh, self.r)

    def init_seg(self, M):
        '''
        将线段树的值初始化为矩阵Matrx
        输入保证Matrx与线段大小一致
        '''
        m0 = M[0]
        self.lazy_tag = 0
        for a in M:
            if a!=m0:
                break
        else:
            self.v = m0
            return
        self.v = '#'
        self.ans = '?'
        midh = self.mid_h
        self.create_subtrees()
        self.left.init_seg(M[:midh-self.l])
        self.right.init_seg(M[midh-self.l:])
    
    def cover_seg(self, l, r, v):
        '''
        将线段[left,right)覆盖为val
        '''
        if self.v == v or l >= self.r or r <= self.l:
            return self.ans
        if l <= self.l and r >= self.r:
            self.v = v
            self.lazy_tag = 0
            self.ans = self.f2(v,self.r-self.l)
            return self.ans
        self.create_subtrees()
        if self.v != '#':
            if self.left:
                self.left.v = self.v
                self.left.ans = self.f2(v,self.left.r-self.left.l)
            if self.right:
                self.right.v = self.v
                self.right.ans = self.f2(v,self.right.r-self.right.l)
            self.v = '#'
        #push up
        self.ans = self.f1(self.left.cover_seg(l, r, v),self.right.cover_seg(l, r, v))
        return self.ans

    def inc_seg(self, l, r, v):
        '''
        将线段[left,right)增加val
        '''
        if v == 0 or l >= self.r or r <= self.l:
            return self.ans
        #self.ans = '?'
        if l <= self.l and r >= self.r:
            if self.v == '#':
                self.lazy_tag += v
            else:
                self.v += v
            self.ans += self.f2(v,self.left.r-self.left.l)
            return self.ans
        self.create_subtrees()
        if self.v != '#':
            self.left.v = self.v
            self.left.ans = self.f2(v,self.left.r-self.left.l)
            self.right.v = self.v
            self.right.ans = self.f2(v,self.right.r-self.right.l)
            self.v = '#'
        self.pushdown()
        self.ans = self.f1(self.left.inc_seg(l, r, v),self.right.inc_seg(l, r, v))
        return self.ans
        
    def pushdown(self):
        if self.lazy_tag != 0:
            if self.left:
                if self.left.v != '#':
                    self.left.v += self.lazy_tag
                    self.left.lazy_tag = 0
                else:
                    self.left.lazy_tag += self.lazy_tag
                self.left.ans += self.f2(self.lazy_tag, self.left.r-self.left.l)
            if self.right:
                if self.right.v != '#':
                    self.right.v += self.lazy_tag
                    self.right.lazy_tag = 0
                else:
                    self.right.lazy_tag += self.lazy_tag
                self.right.ans += self.f2(self.lazy_tag, self.right.r-self.right.l)
            self.lazy_tag = 0

    def query(self, l, r):
        '''
        查询线段[right,bottom)的RMQ
        '''
        if self.ans != '?' and l <= self.l and r >= self.r:
            return self.ans
        if self.v != '#':
            ans = self.f2(self.v, min(r,self.r)-max(l,self.l))
            if l <= self.l and r >= self.r:
                self.ans = ans
            return ans
        self.create_subtrees()
        midh = self.mid_h
        self.pushdown()
        anss = []
        if l < midh:
            anss.append(self.left.query(l, r))
        if r > midh:
            anss.append(self.right.query(l, r))
        ans = reduce(self.f1,anss)
        if l <= self.l and r >= self.r:
            self.ans = ans
        return ans