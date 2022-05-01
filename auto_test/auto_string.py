#string自动测试器
#自动生成string问题的测试用例
#string由26种小写字母组成
#比较两种算法的执行结果
#by BorisTown/ak-bot
import random
import string
from collections import *

def sample_generator(n):
    '''
    随机生成n个测试用例
    '''
    ans = []
    for k in range(1,n+1):
        ans.append("".join([random.choice(string.ascii_lowercase) for i in range(k)]))
    return ans

def F(s):
    ans,suf_sum,pos = 0,0,defaultdict(lambda:-1)
    for i,c in enumerate(s):
        suf_sum += i - pos[c]
        ans += suf_sum
        pos[c] = i
    return int(ans)

def G(s):
    ans,suf_sum,pos = 0,0,defaultdict(lambda:-1)
    for i,c in enumerate(s):
        suf_sum += i - pos[c]
        ans += suf_sum
        pos[c] = i
    return int(ans)

if __name__ == '__main__':
    sp = sample_generator(20)
    ans = []
    for s in sp:
        ans.append(F(s))
    ans2 = []
    for s in sp:
        ans2.append(G(s))
    print([(s,a,b,(a-b)) for s,a,b in zip(sp,ans,ans2)])
    