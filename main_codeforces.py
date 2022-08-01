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

def solve(s,n,S):
    m = len(s)
    M = {}
    for idx,c in enumerate(S):
        l = len(c)
        for i in range(m-l+1):
            if c == s[i:i+l]:
                for pos in range(i,i+l):
                    le2 = l-pos+i
                    if pos not in M:
                        M[pos] = (idx+1,i+1,le2)
                    else:
                        _,_,le = M[pos]
                        if le2 > le:
                            M[pos] = (idx+1,i+1,le2)
    ans = []
    p = 0
    while p<m:
        if p in M:
            a,b,c = M[p]
            ans.append((a,b))
            p+=c
        else:
            return []
    return ans
    
t = int(input()) #input number of test cases
for _ in range(t): #iter for test cases
    s = input()
    n = int(input()) #input int
    S = []
    for _ in range(n):
        S.append(input())
    ans = solve(s,n,S)
    if not ans:
        print(-1)
    else:
        print(len(ans))
        for a,b in ans:
            print(a,b)