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

t = int(input())
for _ in range(t):
    n,m = map(int,input().split()) #input tuple
    def ok(i,j):
        return 0<=i<n and 0<=j<m
    def val(i,j):
        cnt = 0
        for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
            if ok(i+x,j+y):
                cnt += 1
        return cnt
    ans = [[0]*m for _ in range(n)]
    f = True
    for i in range(n):
        L = list(map(int,input().split())) #input list
        for j in range(m):
            ans[i][j] = val(i,j)
            v = L[j]
            if ans[i][j] < v:
                f = False
    if not f:
        print("NO")
    else:
        print("YES")
        for i in range(n):
            print(" ".join(map(str,ans[i])))
    