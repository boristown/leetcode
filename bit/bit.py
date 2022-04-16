# 位运算
# https://oi-wiki.org/math/bit/

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