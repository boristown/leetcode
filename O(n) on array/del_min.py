#从list中删除最少的元素，使它变成……
from collections import *

def del_min_even(L):
    '''
    从L中删除最少的元素，使它：
    变成偶数长度，且由成对的相同的元素连接而成
    时间复杂度：O(n)
    '''
    #分析
    #目标是要让最终的序列变成aabbcc这样……
    #可以分类讨论
    #如果字符串是aaabbccc这样
    #直接保留相邻且相等的元素即可
    #如果是yabcaz这样
    #要保留aa,删除其它字符
    #通用算法：
    #贪心：目标是最大化成对的元素数量
    #对每个元素计数
    #当元素x的数量变成2，重置计数器，配对数量+1
    #答案 = 长度 - 配对数量 * 2
    n = len(L)
    C = Counter()
    m = 0
    for a in L:
        C[a]+=1
        if C[a] == 2:
            C = Counter()
            m+=1
    return n-m*2