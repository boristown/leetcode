'''
布尔序列二分查找工具类
任何二分查找问题都可以抽象为对Bool序列分界点的查找问题
查找[False...False,True...True]序列的第一个True，请使用right方法
查找[True...True,False...False]序列的最后一个True，请使用left方法
需要Python 3.10以上环境
by leetcode-cn.com/u/ak-bot
2022-3-26
'''
class BoolSearch:
    @staticmethod
    def right(l,r,func,param=None):
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
    def left(l,r,func,param=None):
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