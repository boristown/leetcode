from bisect import bisect_right


class BinarySearch:
    '''
    二分查找工具类
    by leetcode-cn.com/u/ak-bot
    2022-3-26
    '''
    @staticmethod
    def bisect_right(l,r,func,param=None):
        '''
        右侧查找
        对于一个形如[False,False,True,True……]的序列
        此方法用于获取右侧第一个True的下标
        [l,r]是查找范围
        func是一个函数，返回指定坐标mid的布尔值
        func的第一个参数是坐标mid,第二个参数是param（可选）
        '''
        if param:
            while l<r:
                mid=(l+r)//2
                if func(mid,param):
                    r=mid
                else:
                    l=mid+1
            return r
        else:
            while l<r:
                mid=(l+r)//2
                if func(mid):
                    r=mid
                else:
                    l=mid+1
            return r

    @staticmethod
    def bisect_left(l,r,func,param=None):
        '''
        左侧查找
        对于一个形如[True,True,False,False……]的序列
        此方法用于获取左侧最后一个True的下标
        [l,r]是查找范围
        func是一个函数，返回指定坐标mid的布尔值
        func的第一个参数是坐标mid,第二个参数是param（可选）
        '''
        if param:
            while l<r:
                mid=(l+r)//2+1
                if func(mid,param):
                    l=mid
                else:
                    r=mid-1
            return l
        else:
            while l<r:
                mid=(l+r)//2+1
                if func(mid):
                    l=mid
                else:
                    r=mid-1
            return l
