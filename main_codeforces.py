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

inf = float("inf")

def solve(m,A):
    M = [(1,0),(0,1),(-1,0),(0,1)]
    dp = [[0]*(m+1) for _ in range(2)]
    dp[0][-1] = 1
    dp[1][-1] = 1
    k = 1
    for j in range(m-1,-1,-1):
        dp[0][j] = max(A[0][j],A[1][j]+k,dp[1][j+1]+1)
        dp[1][j] = max(A[0][j]+k,A[1][j],dp[0][j+1]+1)
        k+=2
    ans2 = inf
    ans = 0
    i,j = 0,0
    for k in range(m*2-1):
        if (j-i) % 2== 0:
            ans2 = min(ans2,max(ans,dp[i][j]+1))
        ans+=1
        x,y = M[k%4]
        i,j = i+x,j+y
        if ans <= A[i][j]:
            ans = A[i][j]+1
    return min(ans,ans2)

def solve3(m,A):
    ans = 0
    for j in range(0,m):
        ans+=1
        if ans <= A[1][j]:
            ans = A[1][j]+1
    for j in range(m-1,0,-1):
        ans+=1
        if ans <= A[0][j]:
            ans = A[0][j]+1
    return ans
    
t = int(input()) #input number of test cases
for _ in range(t): #iter for test cases
    m = int(input()) #input int
    L1 = list(map(int,input().split())) #input list
    L2 = list(map(int,input().split())) #input list
    A = [L1,L2]
    ans = solve(m,A)
    print(ans)