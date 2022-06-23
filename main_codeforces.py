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
from calendar import month_name
from collections import *
from bisect import *
n=int(input())
A=list(map(int,input().split()))
sm = sum(A)
mx = 0
tot = 0
min_v = 1
for a in A:
    tot = (tot + 1) if a == 1 else (tot - 1)
    v = tot - mx
    min_v = min(min_v,v)
    mx = max(mx,tot)
ans = sm - min_v
print(ans)