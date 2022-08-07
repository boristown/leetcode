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

def solve(n,A):
    i,j = 0,n-1
    l,r = -inf,-inf
    while i < n and A[i]>=l:
        l=A[i]
        i+=1
    while j>=0 and A[j]>=r:
        r=A[j]
        j-=1
    return i>j

t = int(input()) #input number of test cases
for _ in range(t): #iter for test cases
    n = int(input()) #input int
    A = list(map(int,input().split())) #input list
    if solve(n,A):
        print("YES")
    else:
        print("NO")