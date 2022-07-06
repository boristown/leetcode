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
t = int(input())
for _ in range(t):
    n = int(input())
    L = list(map(int,input().split())) #input list
    if L[-2]>L[-1]:
        print(-1)
    else:
        d = L[-2]-L[-1]
        for i in range(n-2):
            if L[i]>d:
                L[i]=d
        if 
        print(n-2)
        for i in range(n-2):
            print(i+1,n-1,n)