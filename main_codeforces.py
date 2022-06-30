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
from lzma import FILTER_LZMA2

inf = float("inf")

def solve(n,L):
    ans = 0
    i,j = 0,n-1
    f = L[0]
    f2 = 1-L[0]
    while True:
        while i<=j:
            if f==L[i]:
                i+=1
                f = 1-f
            else:
                break
        while i<=j:
            if f2==L[j]:
                j-=1
                f2 = 1-f2
            else:
                break
        if i <= j:
            f = 1-f
            f2 = 1-f2
            ans += 1
        else:
            break
    return ans

t = int(input()) #input number of test cases
for _ in range(t):
    n = int(input())
    s = input()
    L = list(map(int,list(s))) #input list
    ans = solve(n,L)
    print(ans)