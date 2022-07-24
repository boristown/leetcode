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
import math

inf = float("inf")

def solve(n,m,k,A):
    if A[0] >= nm:
        return True
    B = [a//n for a in A]
    C = [b//2*2 for b in B if b > 1]
    return sum(C) >= m

t = int(input()) #input number of test cases
for _ in range(t): #iter for test cases
    n,m,k = map(int,input().split()) #input tuple
    A = list(map(int,input().split())) #input list
    A.sort(reverse=True)
    nm = n*m
    ans = A[0] >= nm or solve(n,m,k,A) or solve(m,n,k,A)
    if ans: print("Yes")
    else: print("No")