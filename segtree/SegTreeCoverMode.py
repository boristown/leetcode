#todo:修改为动态开点线段树
class SegmentTree:
    '''
    线段树（区间更新+覆盖模式+区间和+区间最大值）
    '''
    def __init__(self, arr, u, v):
        n = v-u+1
        m = (n-1)//2+1
        self.u, self.v = u, v
        if u == v:
            self.label = arr[0]
            self.left = None
            self.right = None
        else:
            self.label = '#'
            self.left = SegmentTree(arr[:m],u,self.mid)
            self.right = SegmentTree(arr[m:],self.mid+1,v)

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
        if self.label != '#':
            self.left.label = self.label
            self.right.label = self.label
            self.label = '#'
        if u <= self.mid:
            self.left.update(t, u, v)
        if self.mid < v:
            self.right.update(t, u, v)

    def querysum(self,u,v):
        '''
        查询[u,v]的区间和
        '''
        if self.label != '#':
            return self.label * (min(v,self.v) - max(u,self.u) + 1)
        ans = 0
        if u <= self.mid:
            ans += self.left.querysum(u, v)
        if self.mid < v:
            ans += self.right.querysum(u, v)
        return ans

    def querymax(self,u,v):
        '''
        查询[u,v]的区间最大值
        '''
        if self.label != '#':
            return self.label
        ans = -float("inf")
        if u <= self.mid:
            ans = max(ans,self.left.querymax(u, v))
        if self.mid < v:
            ans = max(ans,self.right.querymax(u, v))
        return ans

if __name__ == "__main__":
    #初始化线段树为[0,2,3,9,5]
    seg = SegmentTree([0,2,3,9,5],0,4)
    #把坐标2~3设置为7 [0,2,7,7,5]
    seg.update(7,2,3)
    #输出3~4的区间和 12
    print(seg.querysum(3,4))
    #输出3~4的区间最大值 7
    print(seg.querymax(3,4))
    #把坐标0~2设置为4 [4,4,4,7,5]
    seg.update(4,0,2)
    #输出0~4的区间和 24
    print(seg.querysum(0,4))
    #输出0~4的区间最大值 7
    print(seg.querymax(0,4))
    #把坐标3~4设置为11 [4,4,4,11,11]
    seg.update(11,3,4)
    #输出2~3的区间和 15
    print(seg.querysum(2,3))
    #输出2~3的区间最大值 11
    print(seg.querymax(2,3))
    #把坐标1~1设置为8 [4,8,4,11,11]
    seg.update(8,1,1)
    #输出1~2的区间和 12
    print(seg.querysum(1,2))
    #输出1~2的区间和 8
    print(seg.querymax(1,2))