import string
from primes import *
INF = float("inf") #无限
MOD = 1000000007 #力扣取模常数
D4 = [(-1,0),(1,0),(0,-1),(0,1)] #迷宫的4个方向
D8 = [(-1,-1),(1,1),(-1,0),(1,0),(-1,1),(1,-1),(0,-1),(0,1)] #迷宫的8个方向
lowercase = string.ascii_lowercase #小写字母a-z
uppercase = string.ascii_uppercase #大写字母A-Z
letters = string.ascii_letters #字母a-Z
digits = string.digits #数字0123456789
hexdigits = string.hexdigits #16进制字符0123456789abcdefABCDEF
pset = set(primes)