#list自动测试器
#自动生成list问题的测试用例
#list由0到99的数字组成
#比较两种算法的执行结果
#by BorisTown/ak-bot
import random
import string
from collections import *

elements = [i for i in range(100)]

def sample_generator(n):
    '''
    随机生成n个测试用例
    '''
    ans = []
    for k in range(1,n+1):
        ans.append([random.choice(elements) for i in range(k)])
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
    