from functools import reduce

class AreaTree:
    '''
    区域树 by AK自动机
    支持二维空间中的增量更新，覆盖更新，矩阵更新，任意RMQ操作
    基于四叉树实现
    初始化：O(1)
    增量更新或覆盖更新的单次操作复杂度：O(log k)
    序列更新的单次复杂度：O(n)
    当第一个维度长度为1时，区域树退化为线段树，因此区域树也可以当作线段树使用
    https://github.com/boristown/leetcode/blob/main/AreaTree.py
    '''
    def __init__(self, f1, f2, t, b, l, r, v = 0):
        '''
        初始化区域树[top,bottom) [left,right)
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
        self.segmode = (t + 1 == b)
        if not self.segmode:
            self.t = t #top
            self.b = b #bottom
            self.lt = None #SubTree(left,top)
            self.rt = None #SubTree(right,top)
        self.ans = '?'
        self.f1 = f1
        self.f2 = f2
        self.l = l #left
        self.r = r #right
        self.v = v #init value
        self.lazy_tag = 0 #Lazy tag
        self.lb = None #SubTree(left,bottom)
        self.rb = None #SubTree(right,bottom)
    
    @property
    def mid_h(self):
        return (self.l + self.r) // 2

    @property
    def mid_v(self):
        return (self.t + self.b) // 2

    def create_subtrees(self):
        midh = self.mid_h
        if not self.segmode:
            midv = self.mid_v
        if not self.segmode:
            if not self.lt and midv > self.t:
                self.lt = AreaTree(self.f1, self.f2, self.t, midv, self.l, midh)
            if not self.rt and midv > self.t and midh > self.l:
                self.rt = AreaTree(self.f1, self.f2, self.t, midv, midh, self.r)
            if not self.lb and midh > self.l:
                self.lb = AreaTree(self.f1, self.f2, midv, self.b, self.l, midh)
            if not self.rb:
                self.rb = AreaTree(self.f1, self.f2, midv, self.b, midh, self.r)
        else:
            if not self.lb and midh > self.l:
                self.lb = AreaTree(self.f1, self.f2, 0, 1, self.l, midh)
            if not self.rb:
                self.rb = AreaTree(self.f1, self.f2, 0, 1, midh, self.r)


    def init_area(self, M):
        '''
        将区域树的值初始化为矩阵Matrx
        输入保证Matrx与区域大小一致
        '''
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
        self.ans = '?'
        midh = self.mid_h
        if not self.segmode:
            midv = self.mid_v
        self.create_subtrees()
        if not self.segmode:
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
        else:
            Mlb = []
            line = []
            for j in range(self.l, midh):
                line.append(M[0][j-self.l])
            Mlb.append(line)
            self.lb.init_area(Mlb)
            Mrb = []
            line = []
            for j in range(midh, self.r):
                line.append(M[0][j-self.l])
            Mrb.append(line)
            self.rb.init_area(Mrb)
    
    def cover_area(self, t, b, l, r, v):
        '''
        将区域[top,bottom) [left,right)覆盖为val
        '''
        if self.v == v: return
        if not self.segmode:
            if t <= self.t and b >= self.b and l <= self.l and r >= self.r:
                self.v = v
                self.lazy_tag = 0
                self.ans = '?'
                return
        else:
            if l <= self.l and r >= self.r:
                self.v = v
                self.lazy_tag = 0
                self.ans = '?'
                return
        self.ans = '?'
        self.create_subtrees()
        midh = self.mid_h
        if not self.segmode:
            midv = self.mid_v
        if self.v != '#':
            if not self.segmode:
                if self.lt:
                    self.lt.v = self.v
                    self.lt.ans = '?'
                if self.rt:
                    self.rt.v = self.v
                    self.rt.ans = '?'
            if self.lb:
                self.lb.v = self.v
                self.lb.ans = '?'
            if self.rb:
                self.rb.v = self.v
                self.rb.ans = '?'
            self.v = '#'
        if not self.segmode:
            if t < midv and l < midh:
                self.lt.cover_area(t, b, l, r, v)
            if t < midv and r > midh:
                self.rt.cover_area(t, b, l, r, v)
            if b > midv and l < midh:
                self.lb.cover_area(t, b, l, r, v)
            if b > midv and r > midh:
                self.rb.cover_area(t, b, l, r, v)
        else:
            if l < midh:
                self.lb.cover_area(0, 1, l, r, v)
            if r > midh:
                self.rb.cover_area(0, 1, l, r, v)
    
    def pushdown(self):
        if self.lazy_tag != 0:
            if not self.segmode:
                if self.lt:
                    if self.lt.v != '#':
                        self.lt.v += self.lazy_tag
                        self.lt.lazy_tag = 0
                    else:
                        self.lt.lazy_tag += self.lazy_tag
                    self.lt.ans = '?'
                if self.rt:
                    if self.rt.v != '#':
                        self.rt.v += self.lazy_tag
                        self.rt.lazy_tag = 0
                    else:
                        self.rt.lazy_tag += self.lazy_tag
                    self.rt.ans = '?'
            if self.lb:
                if self.lb.v != '#':
                    self.lb.v += self.lazy_tag
                    self.lb.lazy_tag = 0
                else:
                    self.lb.lazy_tag += self.lazy_tag
                self.lb.ans = '?'
            if self.rb:
                if self.rb.v != '#':
                    self.rb.v += self.lazy_tag
                    self.rb.lazy_tag = 0
                else:
                    self.rb.lazy_tag += self.lazy_tag
                self.rb.ans = '?'
            self.lazy_tag = 0

    def inc_area(self, t, b, l, r, v):
        '''
        将区域[top,bottom) [left,right)增加val
        '''
        if v == 0: return
        self.ans = '?'
        if not self.segmode:
            if t <= self.t and b >= self.b and l <= self.l and r >= self.r:
                if self.v == '#':
                    self.lazy_tag += v
                else:
                    self.v += v
                return
        else:
            if l <= self.l and r >= self.r:
                if self.v == '#':
                    self.lazy_tag += v
                else:
                    self.v += v
                return
        self.create_subtrees()
        midh = self.mid_h
        if not self.segmode:
            midv = self.mid_v
        if self.v != '#':
            if not self.segmode:
                self.lt.v = self.v
                self.lt.ans = '?'
                self.rt.v = self.v
                self.rt.ans = '?'
            self.lb.v = self.v
            self.lb.ans = '?'
            self.rb.v = self.v
            self.rb.ans = '?'
            self.v = '#'
        self.pushdown()
        if not self.segmode:
            if t < midv and l < midh:
                self.lt.inc_area(t, b, l, r, v)
            if t < midv and r > midh:
                self.rt.inc_area(t, b, l, r, v)
            if b > midv and l < midh:
                self.lb.inc_area(t, b, l, r, v)
            if b > midv and r > midh:
                self.rb.inc_area(t, b, l, r, v)
        else:
            if l < midh:
                self.lb.inc_area(0, 1, l, r, v)
            if r > midh:
                self.rb.inc_area(0, 1, l, r, v)

    def query(self, t, b, l, r):
        '''
        查询区域[left,top,right,bottom)的RMQ
        '''
        if self.ans != '?' and t <= self.t and b >= self.b and l <= self.l and r >= self.r:
            return self.ans
        if self.v != '#':
            if not self.segmode:
                ans = self.f2(self.v, (min(b,self.b)-max(t,self.t))*(min(r,self.r)-max(l,self.l)))
                if t <= self.t and b >= self.b and l <= self.l and r >= self.r:
                    self.ans = ans
                return ans
            else:
                ans = self.f2(self.v, min(r,self.r)-max(l,self.l))
                if l <= self.l and r >= self.r:
                    self.ans = ans
                return ans
        if not self.segmode:
            if self.ans != '?' and t <= self.t and b >= self.b and l <= self.l and r >= self.r:
                return self.ans
        else:
            if self.ans != '?' and l <= self.l and r >= self.r:
                return self.ans
        self.create_subtrees()
        midh = self.mid_h
        if not self.segmode:
            midv = self.mid_v
        self.pushdown()
        anss = []
        if not self.segmode:
            if t < midv and l < midh:
                anss.append(self.lt.query(t, b, l, r))
            if t < midv and r > midh:
                anss.append(self.rt.query(t, b, l, r))
            if b > midv and l < midh:
                anss.append(self.lb.query(t, b, l, r))
            if b > midv and r > midh:
                anss.append(self.rb.query(t, b, l, r))
        else:
            if l < midh:
                anss.append(self.lb.query(0, 1, l, r))
            if r > midh:
                anss.append(self.rb.query(0, 1, l, r))
        ans = reduce(self.f1,anss)
        if not self.segmode:
            if t <= self.t and b >= self.b and l <= self.l and r >= self.r:
                self.ans = ans
        else:
            if l <= self.l and r >= self.r:
                self.ans = ans
        return ans

if __name__ == '__main__':
    #测试：线段树模式
    #输入:0,3,[1,3,4,2],cover(1,3,10),quert(sum,2,4),inc(2,4,5),,quert(sum,2,4)
    f1 = lambda a,b:a+b
    f2 = lambda a,n:a*n
    AT = AreaTree(f1,f2,0,1,0,4)
    AT.init_area([[1,3,4,2]])
    AT.cover_area(0,1,1,3,10)
    ans = AT.query(0,1,2,4)
    print(ans)
    AT.inc_area(0,1,2,4,5)
    ans = AT.query(0,1,2,4)
    print(ans)
    AT.inc_area(0,1,0,4,-1)
    ans = AT.query(0,1,0,4)
    print(ans)