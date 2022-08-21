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
#    A = list(map(int,input().split())) #input list
#    s = input() #input string
#    ans = solve(s,L) #solve
#    print(ans) #print single answer
#    print(" ".join(map(str,ans))) #print int array
#
#end of codeforces template
#begin of codeforces template code
from bisect import *
from collections import *
from itertools import *

Yes = "Yes"
No = "No"

MOD = 998244353

inf = float("inf")

def read_strs(rows):
    ss = []
    for _ in range(rows):
        ss.append(input())
    return ss

def read_lists(rows):
    lists = []
    for _ in range(rows):
        lists.append(read_list()) #input list
    return lists

def read_list():
    return list(map(int,input().split()))

def read_tuple():
    return map(int,input().split()) #input tuple

def presum(A):
    pre = [0]
    s = 0
    for a in A:
        s += a
        pre.append(s)
    return pre

def sufsum(A):
    suf = [0]
    s = 0
    for a in A[::-1]:
        s += a
        suf.append(s)
    return suf[::-1]
#end of codeforces template code

def solve(N,M,A,B,C,D,E,F,XY):
    ST = set()
    for x,y in XY:
        ST.add((x,y))
    cache = {}
    def dp(i,j,k):
        if (i,j,k) in cache:
            return cache[i,j,k]
        if (i,j) in ST:
            cache[i,j,k] = 0
            return 0
        if k == 0:
            cache[i,j,k] = 1
            return 1
        ans = 0
        ans = (ans + dp(i+A,j+B,k-1) + dp(i+C,j+D,k-1) + dp(i+E,j+F,k-1))%MOD
        cache[i,j,k] = ans
        return ans
    return dp(0,0,N)
        

N,M = read_tuple()
A,B,C,D,E,F = read_tuple()
XY = read_lists(M)
print(solve(N,M,A,B,C,D,E,F,XY))