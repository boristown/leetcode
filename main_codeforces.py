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
import math

inf = float("inf")

t = int(input()) #input number of test cases
for _ in range(t): #iter for test cases
    n,k = map(int,input().split()) #input tuple
    A = list(map(int,input().split())) #input list
    A.sort(reverse=True)
    ans = inf
    mx,mn = A[0],A[-1]//k
    for a in range(max(1,mn),mx+1):
        mna,mxa = inf,-inf
        for i in range(n):
            d = A[i]/a
            d1,d2 = max(1,min(k,math.ceil(d))),min(k,max(math.floor(d),1))
            c1,c2 = A[i]//d1,A[i]//d2
            if abs(c1-a)>abs(c2-a):
                c1,c2=c2,c1
            mna,mxa = min(mna,c1),max(mxa,c1)
        an = mxa-mna
        if an < ans:
            ans = an
    print(ans)