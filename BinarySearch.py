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
