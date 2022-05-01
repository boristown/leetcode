#string自动优化器
#自动生成string问题的O(n)算法（只要算法存在，就能自动生成）
#string由26种小写字母组成
#输出一个整数int
#by BorisTown/ak-bot

#输入：朴素算法
#输出：O(n)算法

#原理：暴力枚举代码组合直到找到解决方案
import random
import string

def sample_generator(n):
    '''
    随机生成n个测试用例
    '''
    ans = []
    for k in range(1,n+1):
        ans.append("".join([random.choice(string.ascii_lowercase) for i in range(k)]))
    return ans

def auto_string(F):
    def G(s):
        return F(s)
    return lambda s:G(s)

if __name__ == '__main__':
    print(sample_generator(20))