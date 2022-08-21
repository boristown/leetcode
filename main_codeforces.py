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

def solve(n,m):
    if n<m:
        n,m=m,n
    ans = (m-1)*2
    if n > 1:
        ans += n
    return ans

t = int(input()) #input number of test cases
for _ in range(t):
    n,m = map(int,input().split()) #input tuple
    ans = solve(n,m)
    print(ans)
