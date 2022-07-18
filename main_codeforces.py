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

from collections import *

inf = float("inf")

t = int(input()) #input number of test cases
for _ in range(t): #iter for test cases
    n = int(input()) #input int
    L = list(map(int,input().split())) #input list
    def solve(i):
        if i >= n-1:
            return 0
        return max(max(L[i-1],L[i+1])+1-L[i],0)
    dp = [0]*(n+1)
    for i in range(n-2,0,-2):
        dp[i] = solve(i) + dp[i+2]
    def F(n,j):
        if n < 3: return 0
        if n%2==1:
            return dp[j+1]
        else:
            ans1 = solve(j+1) + F(n-2,j+2)
            ans2 = solve(j+2) + F(n-3,j+3)
            return min(ans1,ans2)
    print(F(n,0))