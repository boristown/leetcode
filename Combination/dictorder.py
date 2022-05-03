from Combination.basic import MultiInverse
from segtree.SegSumTree import SegSumTree

def dictorder(s,mod):
    '''
    字符串s（仅含小写字母）在全排列中的字典序的mod模
    适用场景：求字符串在全排列中的字典序
    '''
    s = [ord(c)-ord('a') for c in s]
    #排列数（含重复项）公式
    #N = a!/(a1! * a2! *a3!)
    #字符串     c           b           a
    #计数n      3           2           1
    #计数c      1           0           0
    #计数b      1           1           0
    #计数a      1           1           1
    #分子nume   (3-1)!(1+1) (2-1)!1     (1-1)!0
    #分母deno   1!1!1!      1!1!        1!
    #答案ans    4           1           0
    segs = SegSumTree([0]*26)
    n = 0
    nume = 1
    deno = 1
    ct = [0]*26
    ans = 0
    for v in s[::-1]:
        if n>0:
            nume = nume * n % mod
        n+=1
        ct[v]+=1
        #使用乘法逆元将除法转为乘法
        deno=deno * MultiInverse(ct[v],mod) % mod
        segs.update(v,ct[v])
        if v>0:
            nume2 = nume * segs.sumRange(0,v-1)
            ans = (ans + nume2 * deno % mod) % mod
    return ans