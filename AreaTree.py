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
        self.l = l #left
        self.t = t #top
        self.r = r #right
        self.b = b #bottom
        self.v = v #init value
        self.lt = None #SubTree(left,top)
        self.rt = None #SubTree(right,top)
        self.lb = None #SubTree(left,bottom)
        self.rb = None #SubTree(right,bottom)
    
    @property
    def mid_h(self):
        return (self.l + self.r) // 2

    @property
    def mid_v(self):
        return (self.t + self.b) // 2

    def init_area(self, t, b, l, r, M):
        '''
        将区域[top,bottom) [left,right)的值初始化为矩阵Matrx
        输入保证Matrx与区域大小一致
        '''
        m0 = M[0][0]
        diff = False
        for i in range(t,b+1):
            for j in range(l,r+1):
                if M[i][j]!=m0:
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
        Mlt,Mrt,Mlb,Mrb = [],[],[],[]
        if t+1 < b:
            if l+1 < r:
                for i in range(t, midv):
                    line = []
                    for j in range(l, midh):
                        line.append(M[i][j])
                    Mlt.append(line)
                self.lt = AreaTree(t, midv, l, midh)
                self.lt.init_area(t, midv, l, midh, Mlt)
            for i in range(t, midv):
                line = []
                for j in range(midh, r):
                    line.append(M[i][j])
                Mrt.append(line)
            self.rt = AreaTree(t, midv, midh, r)
            self.rt.init_area(t, midv, midh, r, Mrt)
        if l+1 < r:
            for i in range(midv, b):
                line = []
                for j in range(l, midh):
                    line.append(M[i][j])
                Mlb.append(line)
            self.lb = AreaTree(midv, b, l, midh)
            self.lb.init_area(midv, b, l, midh, Mlb)
        for i in range(midv, b):
            line = []
            for j in range(midh, r):
                line.append(M[i][j])
            Mrb.append(line)
        self.rb = AreaTree(midv, b, midh, r)
        self.rb.init_area(midv, b, midh, r, Mrb)
    
    def cover_area(self, t, b, l, r, v):
        '''
        将区域[top,bottom) [left,right)覆盖为val
        '''
        pass

    def inc_area(self, t, b, l, r, v):
        '''
        将区域[top,bottom) [left,right)增加val
        '''
        pass
    
    def query(self, t, b, l, r, func):
        '''
        查询区域[left,top,right,bottom)的func
        fun示例：
        区域和:lambda a,b:a+b
        区域最大值:lambda a,b:max(a,b)
        区域最小值:lambda a,b:min(a,b)
        区域最小值:lambda a,b:min(a,b)
        '''
        pass
