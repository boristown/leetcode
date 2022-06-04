#begin of codeforces template
# (don't delete):
#  
# from collections import *
# from heapq import *
# import bisect
#
#t = int(input()) #input number of test cases
#for _ in range(t): #iter for test cases
#    n = int(input()) #input int
#    n,m = map(int,input().split()) #input tuple
#    L = list(map(int,input().split())) #input list
#    s = input() #input string
#    ans = solve(s,L) #solve
#    print(ans)
#
#end of codeforces template 

def allone(n):
    return (1<<n)-1
    
def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

def modPowerOfTwo(x, mod):
    return x & (mod - 1)

def getBit(a, b):
    return (a >> b) & 1

def unsetBit(a, b):
    return a & ~(1 << b)

def setBit(a, b):
    return a | (1 << b)

def flapBit(a, b):
    return a ^ (1 << b)

def popcount(x):
    cnt = 0
    while x:
        cnt += x & 1
        x >>= 1
    return cnt

def any2dec(origin, x):
    return int(str(origin), base = x)

n = int(input()) #input int
for q in range(n): #iter for test cases
    a = int(input()) #input int
    ans = []
    pc = popcount(a)
    if a == 1:
        print(3)
        continue
    elif pc == 1:
        ans.append('1')
        while a:
            a=a>>1
            if a%2:
                ans.append('1')
                break
            else:
                ans.append('0')
        print(any2dec("".join(ans[::-1]),2))
        continue
    else:
        while a:
            if a%2:
                ans.append('1')
                break
            else:
                ans.append('0')
            a=a>>1
        print(any2dec("".join(ans[::-1]),2))