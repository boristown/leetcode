#begin of codeforces template
# (don't delete):
#  
# from collections import *
# from sortedcontainers import *
# from heapq import *
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


def solve(r):
    if r<=1399:
        return "Division 4"
    elif r<=1599:
        return "Division 3"
    elif r<=1899 :
        return "Division 2"
    else:
        return "Division 1"

t = int(input())
for _ in range(t): #iter for test cases
    rating = int(input()) #input int
    ans = solve(rating)
    print(ans)