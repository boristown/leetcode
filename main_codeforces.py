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

def issorted(A):
    n = len(A)
    for i in range(n-1):
        if A[i]>A[i+1]:
            return False
    return True
    
def solve(n,x,L):
    if x*2<=n:
        return "YES"
    if n == x:
        return "YES" if issorted(L) else "NO"
    l=n-x
    r=x-1
    B = L[l:r+1]
    if not issorted(B):
        return 'NO'
    A = L[:l] + L[r+1:]
    A.sort()
    l0,r0 = A[l-1],A[l]
    l1,r1 = L[l],L[r]
    if l0<=l1 <= r1 <= r0:
        return "YES"
    return "NO"

inf = float("inf")
t = int(input())
for _ in range(t):
    n,x = map(int,input().split()) #input tuple
    L = list(map(int,input().split())) #input list
    ans = solve(n,x,L)
    print(ans)