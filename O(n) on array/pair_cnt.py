#值相等的元素对(i,j)的数量
#https://codeforces.com/problemset/problem/50/B
#*1500
from collections import *

def pair_cnt(L):
    '''
    找出L中值相等的元素对的数量
    '''
    #分析：
    #观察长度n的列表增加为长度n+1后，元素对的变化
    #假设增加的元素为e,且前n个元素中有m个e
    #那么F(n+1) = F(n) + m * 2 + 1
    C = Counter()
    ans = 0
    for i,a in enumerate(L):
        ans += C[a]*2+1
        C[a]+=1
    return ans