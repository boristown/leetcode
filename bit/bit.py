# 位运算
# https://oi-wiki.org/math/bit/

def allone(n):
    '''
    获取一个二进制长度为n且全是1的数字
    '''
    return (1<<n)-1
    
#判断一个数是不是2的非负整数次幂
def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

#对2的非负整数次幂取模：
def modPowerOfTwo(x, mod):
    return x & (mod - 1)

#获取一个数二进制的某一位：
# 获取 a 的第 b 位，最低位编号为 0
def getBit(a, b):
    return (a >> b) & 1

#将一个数二进制的某一位设置为0：
# 将 a 的第 b 位设置为 0 ，最低位编号为 0
def unsetBit(a, b):
    return a & ~(1 << b)

# 将一个数二进制的某一位设置为1：
# 将 a 的第 b 位设置为 1 ，最低位编号为 0
def setBit(a, b):
    return a | (1 << b)

# 将一个数二进制的某一位取反：
# 将 a 的第 b 位取反 ，最低位编号为 0
def flapBit(a, b):
    return a ^ (1 << b)

# 求 x 的汉明权重
def popcount(x):
    cnt = 0
    while x:
        cnt += x & 1
        x >>= 1
    return cnt

def any2dec(origin, x):
    '''
    m: int 
	origin：str
	return: int
    任意进制的数转换为10机制
    直接利用int的自带功能
    适用场景：进制转换
    '''
    return int(str(origin), base = x) # origin必须是字符串

def dec2any(n,x):
    '''
    10进制转N进制
    n为待转换的十进制数，x为机制，取值为2-16
    适用场景：进制转换
    '''
    a=['0','1','2','3','4','5','6','7','8','9','A','b','C','D','E','F']
    b=[]
    while True:
        s=n//x  # 商
        y=n%x  # 余数
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    x=""
    for i in b:
        x+=a[i]
    return x