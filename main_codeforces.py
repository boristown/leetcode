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
from itertools import *

inf = float("inf")

def solve(n,A):
    I = defaultdict(list)
    preMax = []
    maxE = []
    for i,a in enumerate(A):
        I[a].append(i)
        maxE.append(len(I))
    mx = 0
    for i,a in enumerate(A):
        mx = max(mx,I[a][-1])
        preMax.append(mx)

    for i in range(n-2,-1,-1):
        a,b = A[i],A[i+1]
        if a>b: #key point
            k=preMax[i]
            ans = maxE[k]
            #print("ans:",i,preMax,k,maxE,ans)
            return ans
    return 0

MAX = 10**9
t = int(input()) #input number of test cases
for _ in range(t): #iter for test cases
    n,k = map(int,input().split()) #input tuple
    A = list(map(int,input().split())) #input list
    P = [(a,i) for i,a in enumerate(A)]
    P.sort()
    if n == k:
        print(MAX)
    else:
        if n == 2:
            print(max(A))
        else:
            if k == 1:
                minsuf = min(A[2:])
                minpre = min(A[:-2])
                ans1 = min(A[0],minsuf*2)
                ans2 = min(A[-1],minpre*2)
                ans4 = min(A[1],minsuf*2)
                ans5 = min(A[-2],minpre*2)
                ans3 = max(A)
                print(max(ans1,ans2,ans3,ans4,ans5))
            else:
                S = set()
                for i in range(k):
                    p = P[i][1]
                    f = False
                    if p-1 in S or p+1 in S:
                        f=True
                    S.add(p)
                if f:
                    ans = P[k][0]*2
                else:
                    ans = P[k-1][0]*2
                print(min(ans,MAX))