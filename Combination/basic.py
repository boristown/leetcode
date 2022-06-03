from functools import *

MOD = 10**9+7

def MultiInverse(x,mod):
    '''
    乘法逆元
    适用场景：将除法模运算转化为乘法
    '''
    return pow(x,mod-2,mod)

def BigDivision(x,y,mod):
    '''
    大数除法x/y
    适用场景：快速计算大数相除（取模）
    '''
    return (x % mod) * MultiInverse(y) % mod
    
@cache
def fact(x):
    '''
    x的阶乘
    适用场景：计算排列组合数
    '''
    if x < 1: return 0
    if x == 1: return 1
    return x*fact(x-1)

@cache
def fact2(x,y):
    '''
    从y+1到x的阶乘
    适用场景：计算排列组合数
    '''
    return fact(x)//fact(y)

@cache
def A(n,m):
    '''
    从n个元素中选择m个排列数
    适用场景：计算排列数
    '''
    ans = 1
    for i in range(n,n-m,-1):
        ans *= i
    return ans

@cache
def C(n,m):
    '''
    从n个元素中选择m个组合数
    适用场景：计算组合数
    '''
    ans = A(n,m)
    x = 1
    for i in range(1,m+1):
        x *= i
    return ans // x

@cache
def Amod(n,m,mod):
    '''
    从n个元素中选择m个排列数(结果取模)
    适用场景：计算排列数
    '''
    ans = 1
    for i in range(n,n-m,-1):
        ans = (ans * i) % mod
    return ans

@cache
def Cmod(n,m,mod):
    '''
    从n个元素中选择m个组合数(结果取模)
    适用场景：计算组合数
    '''
    ans = Amod(n,m,mod)
    x = 1
    for i in range(1,m+1):
        x = (x * MultiInverse(i,mod)) % mod
    return (ans * x) % mod

@cache
def Amod(n,m,mod):
    '''
    从n个元素中选择m个排列数(结果取模)
    适用场景：计算排列数
    '''
    ans = 1
    for i in range(n,n-m,-1):
        ans = (ans * i) % mod
    return ans

@cache
def Cmod(n,m,mod):
    '''
    从n个元素中选择m个组合数(结果取模)
    适用场景：计算组合数
    '''
    ans = Amod(n,m,mod)
    x = 1
    for i in range(1,m+1):
        x = (x * MultiInverse(i,mod)) % mod
    return (ans * x) % mod

@cache
def _Amod(n,m):
    '''
    从n个元素中选择m个排列数(结果取模)
    递归写法
    适用场景：计算排列数
    '''
    if m == 0: return 1
    return (_Amod(n-1,m-1)*n)%MOD

@cache
def _Cmod(n,m):
    '''
    从n个元素中选择m个组合数(结果取模)
    递归写法
    适用场景：计算组合数
    '''
    if m == 0: return 1
    return _Cmod(n-1,m-1) * n // m

def Cmod2(n):
    '''
    从n个元素中选择任意个数的组合数
    '''
    return 1<<n