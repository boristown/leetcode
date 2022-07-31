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

from collections import *
from functools import *
import math

inf = float("inf")

MOD = 998244353

n = int(input()) #input number of test cases
A = list(map(int,input().split())) #input list
ans = 0

def dp(i,a,b,c):
    if a == 0:
        if c == 0:
            return 1
        else:
            return 0
    n1 = n - i
    if n1 < a:
        return 0
    r = A[i]%b
    c2=(c+r)%b
    ans1 = dp(i+1,a-1,b,c2)
    ans2 = dp(i+1,a,b,c)
    return ans1+ans2
    
for a in range(1,n+1):
    ans += dp(0,a,a,0)
print(ans%MOD)