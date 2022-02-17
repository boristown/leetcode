from itertools import *
from functools import *

def elements_max_split(E):
    '''
    从元素中选出两个和相同的子集，最大化这样的子集
    E:元素清单
    :返回符合条件的子集的最大大小
    '''
    @cache(None)
    def dp(i, s):
        if i == len(E):
            return 0 if s == 0 else float('-inf')
        return max(dp(i + 1, s), dp(i + 1, s - E[i]), dp(i + 1, s + E[i]) + E[i])
    return dp(0, 0)