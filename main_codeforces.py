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
#    print(ans)
#
#end of codeforces template

from bisect import *
from collections import *

inf = float("inf")

def solve(n,m,A):
    ans = []
    if n == 1:
        if int(A[0][-1])%2==1:
            return [1]
        else:
            return []
    s = 0
    na = 0
    for i in range(n):
        s += int(A[i][-1])%2
        if s%2 == 1 and na<m-1:
            ans.append(i+1)
            na += 1
            s = 0
    if s%2 == 1:
        ans.append(n)
    if len(ans)==m:
        return ans
    else:
        return []

t = int(input())
for _ in range(t):
    n,m = map(int,input().split()) #input tuple
    if n == 1:
        a = input()
        A = [a]
    else:
        A = input().split() #input list
    ans = solve(n,m,A)
    if ans:
        print("YES")
        print(" ".join(map(str,ans)))
    else:
        print("NO")