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

inf = float("inf")

t = int(input()) #input number of test cases
for _ in range(t): #iter for test cases
    n = int(input()) #input int
    L = list(map(int,input().split())) #input list
    if L[0] < L [-1]:
        print("YES")
    else:
        print("NO")