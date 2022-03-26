from bisect import *

class BoolSearch:
    '''
    布尔序列二分查找工具类
    任何二分查找问题都可以抽象为对Bool序列分界点的查找问题
    查找[False...False,True...True]序列的第一个True，请使用right方法
    查找[True...True,False...False]序列的最后一个True，请使用left方法
    需要Python 3.10以上环境
    by leetcode-cn.com/u/ak-bot
    2022-3-26
    '''
    @staticmethod
    def right(l,r,func,param=None):
        '''
        查找右侧第一个True
        对于一个形如[False...False,True...True]的序列
        此方法用于获取右侧第一个True的下标
        [l,r]是查找范围
        func是一个函数，返回指定坐标mid的布尔值
        func的第一个参数是坐标mid,第二个参数是param（可选）
        '''
        if param:
            return bisect_right(range(l,r+1),False,lambda x:func(x,param))
        else:
            return bisect_right(range(l,r+1),False,lambda x:func(x))

    @staticmethod
    def left(l,r,func,param=None):
        '''
        查找左侧最后一个True
        对于一个形如[True...True,False...False]的序列
        此方法用于获取左侧最后一个True的下标
        [l,r]是查找范围
        func是一个函数，返回指定坐标mid的布尔值
        func的第一个参数是坐标mid,第二个参数是param（可选）
        '''
        if param:
            return bisect_left(range(l,r+1),True,lambda x:not func(x,param))-1
        else:
            return bisect_left(range(l,r+1),True,lambda x:not func(x))-1
