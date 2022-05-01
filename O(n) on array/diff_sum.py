from collections import *

def diff_sum(L,mod=float("inf")):
    '''
    统计列表L中的所有子列表L1中的不同元素的总数(对mod取模)
    时间复杂度：O(n)
    '''
    #分析：
    #定义F(k)为列表L[:k]中的答案
    #定义G(M)为列表M中不同元素的个数
    #G(M) = has(M,'a')+ …… +has(M,'z')
    #F(0) = 1
    #F(1) = F(0) + G(L[0:2]) + 1
    #F(2) = F(1) + G(L[0:3]) + G(L[1:3]) + 1
    #F(3) = F(2) + G(L[0:4]) + G(L[1:4]) + G(L[2:4]) + 1
    #F(4) = F(3) + G(L[0:5]) + G(L[1:5]) + G(L[2:5]) + G(L[3:5]) + 1
    #作差：
    #D(0) = F(1) - F(0) = G(L[0:2]) + 1
    #D(1) = F(2) - F(1) = G(L[0:3]) + G(L[1:3]) + 1
    #D(2) = F(3) - F(2) = G(L[0:4]) + G(L[1:4]) + G(L[2:4]) + 1
    #D(3) = F(4) - F(3) = G(L[0:5]) + G(L[1:5]) + G(L[2:5]) + G(L[3:5]) + 1
    #再作差：
    #E(0) = D(1) - D(0) = G(L[0:3]) - G(L[0:2]) + G(L[1:3]) = 1 - pos[e]
    #E(1) = D(2) - D(1) = G(L[0:4]) + G(L[1:4]) + G(L[2:4]) - G(L[0:3]) - G(L[1:3]) = 2 - pos[e]
    #E(2) = D(3) - D(2) = G(L[0:5]) + G(L[1:5]) + G(L[2:5]) + G(L[3:5]) - G(L[0:4]) - G(L[1:4]) - G(L[2:4]) = 3 - pos[e]
    #公式引入：
    #设L[k] = e
    #如果L[i:k]中含有元素e：则G(L[i:k]) = G([i:k+1])
    #反之：G(L[i:k]) = G([i:k+1])+1
    ans,tot,pos = 0,0,defaultdict(lambda:-1)
    for i,c in enumerate(L):
        tot += i - pos[c] #通过e的当前坐标与前一个坐标的差值，计算tot增量
        ans += tot
        pos[c] = i
    return int(ans % mod)