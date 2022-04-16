class SegmentTree:
    def __init__(self, u, v):
        self.u, self.v = u, v
        self.label = 0
        if u == v:
            self.left = None
            self.right = None
        else:
            self.left = SegmentTree(u, self.mid)
            self.right = SegmentTree(self.mid + 1, v)

    @property
    def mid(self):
        return (self.u + self.v) // 2

    def update(self, t, u, v):
        '''
        将[u,v]之间的数字更新为t
        '''
        if u <= self.u and self.v <= v:
            self.label = t
            return
        if self.label != -1:
            self.left.label = self.label
            self.right.label = self.label
            self.label = -1
        if u <= self.mid:
            self.left.update(t, u, v)
        if self.mid < v:
            self.right.update(t, u, v)

    def query(self):
        '''
        查询和
        '''
        if self.label != -1:
            return self.label * (self.v - self.u + 1)
        return self.left.query() + self.right.query()