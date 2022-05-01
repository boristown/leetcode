from collections import *

def diff_sum(L,mod=float("inf")):
    '''
    统计列表L中的所有子列表L1中的不同元素的总数(对mod取模)
    时间复杂度：O(n)
    '''
    ans,tot,pos = 0,0,defaultdict(lambda:-1)
    for i,c in enumerate(L):
        tot += i - pos[c] #通过e的当前坐标与前一个坐标的差值，计算tot增量
        ans += tot
        pos[c] = i
    return int(ans % mod)