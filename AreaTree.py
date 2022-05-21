from itertools import reduce

class AreaTree:
    '''
    区域树 by AK自动机
    支持二维空间中的增量更新，覆盖更新，矩阵更新，任意RMQ操作
    基于四叉树实现
    初始化：O(1)
    增量更新或覆盖更新的单次操作复杂度：O(log k)
    序列更新的单次复杂度：O(n)
    当区域宽度为1时，区域树退化为线段树，因此区域树也可以当作线段树使用
    https://github.com/boristown/leetcode/blob/main/AreaTree.py
    '''
    def __init__(self, t, b, l, r, v = 0):
        '''
        初始化区域树[top,bottom) [left,right)
        '''
        if t >= b or l >= r:
            self.end = True
            return
        self.l = l #left
        self.t = t #top
        self.r = r #right
        self.b = b #bottom
        self.v = v #init value
        self.lazy_tag = 0 #Lazy tag
        self.lt = None #SubTree(left,top)
        self.rt = None #SubTree(right,top)
        self.lb = None #SubTree(left,bottom)
        self.rb = None #SubTree(right,bottom)
        self.end = False #End node
    
    @property
    def mid_h(self):
        return (self.l + self.r) // 2

    @property
    def mid_v(self):
        return (self.t + self.b) // 2

    def create_subtrees(self):
        if self.end: return
        midh = self.mid_h
        midv = self.mid_v
        if not self.lt:
            self.lt = AreaTree(self.t, midv, self.l, midh)
        if not self.lb:
            self.lb = AreaTree(midv, self.b, self.l, midh)
        if not self.rt:
            self.rt = AreaTree(self.t, midv, midh, self.r)
        if not self.rb:
            self.rb = AreaTree(midv, self.b, midh, self.r)

    def init_area(self, M):
        '''
        将区域树的值初始化为矩阵Matrx
        输入保证Matrx与区域大小一致
        '''
        if self.end:
            return
        m0 = M[0][0]
        self.lazy_tag = 0
        diff = False
        for line in M:
            for a in line:
                if a!=m0:
                    diff = True
                    break
            if diff:
                break
        else:
            self.v = m0
            return
        self.v = '#'
        midh = self.mid_h
        midv = self.mid_v
        self.create_subtrees()
        Mlt = []
        for i in range(self.t, midv):
            line = []
            for j in range(self.l, midh):
                line.append(M[i-self.t][j-self.l])
            Mlt.append(line)
        self.lt.init_area(Mlt)
        Mrt = []
        for i in range(self.t, midv):
            line = []
            for j in range(midh, self.r):
                line.append(M[i-self.t][j-self.l])
            Mrt.append(line)
        self.rt.init_area(Mrt)
        Mlb = []
        for i in range(midv, self.b):
            line = []
            for j in range(self.l, midh):
                line.append(M[i-self.t][j-self.l])
            Mlb.append(line)
        self.lb.init_area(Mlb)
        Mrb = []
        for i in range(midv, self.b):
            line = []
            for j in range(midh, self.r):
                line.append(M[i-self.t][j-self.l])
            Mrb.append(line)
        self.rb.init_area(Mrb)
    
    def cover_area(self, t, b, l, r, v):
        '''
        将区域[top,bottom) [left,right)覆盖为val
        '''
        if self.end:
            return
        if t <= self.t and b >= self.b and l <= self.l and r >= self.r:
            self.v = v
            self.lazy_tag = 0
            return
        self.create_subtrees()
        midh = self.mid_h
        midv = self.mid_v
        if self.v != '#':
            self.lt.v = self.v
            self.lb.v = self.v
            self.rt.v = self.v
            self.rb.v = self.v
            self.v = '#'
        if t < midv and l < midh:
            self.lt.cover_area(t, b, l, r, v)
        if b > midv and l < midh:
            self.lb.cover_area(t, b, l, r, v)
        if t < midv and r > midh:
            self.rt.cover_area(t, b, l, r, v)
        if b > midv and r > midh:
            self.rb.cover_area(t, b, l, r, v)
    
    def pushdown(self):
        if self.lazy_tag != 0:
            if self.lt.v != '#':
                self.lt.v += self.lazy_tag
                self.lt.lazy_tag = 0
            else:
                self.lt.lazy_tag += self.lazy_tag
            if self.lb.v != '#':
                self.lb.v += self.lazy_tag
                self.lb.lazy_tag = 0
            else:
                self.lb.lazy_tag += self.lazy_tag
            if self.rt.v != '#':
                self.rt.v += self.lazy_tag
                self.rt.lazy_tag = 0
            else:
                self.rt.lazy_tag += self.lazy_tag
            if self.rb.v != '#':
                self.rb.v += self.lazy_tag
                self.rb.lazy_tag = 0
            else:
                self.rb.lazy_tag += self.lazy_tag
            self.lazy_tag = 0

    def inc_area(self, t, b, l, r, v):
        '''
        将区域[top,bottom) [left,right)增加val
        '''
        if self.end:
            return
        if t <= self.t and b >= self.b and l <= self.l and r >= self.r:
            if self.v == '#':
                self.lazy_tag += v
            else:
                self.v += v
            return
        self.create_subtrees()
        midh = self.mid_h
        midv = self.mid_v
        if self.v != '#':
            self.lt.v = self.v
            self.lb.v = self.v
            self.rt.v = self.v
            self.rb.v = self.v
            self.v = '#'
        self.pushdown()
        if t < midv and l < midh:
            self.lt.inc_area(t, b, l, r, v)
        if b > midv and l < midh:
            self.lb.inc_area(t, b, l, r, v)
        if t < midv and r > midh:
            self.rt.inc_area(t, b, l, r, v)
        if b > midv and r > midh:
            self.rb.inc_area(t, b, l, r, v)
    
    def query(self, t, b, l, r, f1, f2):
        '''
        查询区域[left,top,right,bottom)的f1
        f1,f2示例：
        区域和:
        f1:lambda a,b:a+b 
        f2:lambda a,n:a*n
        区域最大值:
        f1:lambda a,b:max(a,b)
        f2:lambda a,n:a
        区域最小值:
        f1:lambda a,b:min(a,b)
        f2:lambda a,n:a
        '''
        if self.end: return '#'
        if self.v != '#':
            return f2(self.v, (min(b,self.b)-max(t,self.t))*(min(r,self.r)-max(l,self.l)))
        self.create_subtrees()
        midh = self.mid_h
        midv = self.mid_v
        self.pushdown()
        ans = []
        if t < midv and l < midh:
            ans.append(self.lt.query(t, b, l, r, f1, f2))
        if b > midv and l < midh:
            ans.append(self.lb.query(t, b, l, r, f1, f2))
        if t < midv and r > midh:
            ans.append(self.rt.query(t, b, l, r, f1, f2))
        if b > midv and r > midh:
            ans.append(self.rb.query(t, b, l, r, f1, f2))
        return reduce(f1,ans)