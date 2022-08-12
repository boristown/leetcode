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

from heapq import *
t = int(input())
hp = []
for _ in range(t):
    s = input()
    if s[0] == '1':
        heappush(hp,int(s[2:]))
    elif s[0] == '2':
        print(hp[0])
    elif s[0] == '3':
        heappop(hp)