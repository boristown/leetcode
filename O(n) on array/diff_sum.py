from collections import *

def diff_sum(L,mod=float("inf")):
    '''
    统计列表L中的所有子列表L1中的不同元素的总数(对mod取模)
    时间复杂度：O(n)
    '''
    #分析：
    #观察当在列表L1的末尾增加一个元素e1，形成列表L2时，答案的变化:
    #由于列表L2包含列表L1，因此ans(L2) = ans(L1) + suf_sum(L1,e1)
    #suf_sum(L1,e1)是L1的后缀与e1连接的子列表中的不同元素的数量
    #观察向列表末尾增加元素时，suf_sum的变化：
    #当向列表末尾增加元素是，所有后缀的长度都加1了，因此：
    #suf_sum(L2,e2) = suf_sum(L2,e2) + i - pos[e2]
    #其中pos[e2]是e2上一次出现的坐标，只有在这之后的后缀，不同元素的数量才会增加，
    #因此用i-pos[e2]计算suf_sum增加的值
    ans,tot,pos = 0,0,defaultdict(lambda:-1)
    for i,c in enumerate(L):
        tot += i - pos[c] #通过e的当前坐标与前一个坐标的差值，计算tot增量
        ans += tot
        pos[c] = i
    return int(ans % mod)