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

def solve(s,t):
    ans = list(s)
    i = len(s) - 1
    while i>=0:
        a = s[i]
        if a == 'z':
            b = 'a'
            ans[i] = b
            i-=1
        else:
            b = chr(ord(a)+1)
            ans[i] = b
            break
    ans2 = "".join(ans)
    if ans2>=t:
        return "No such string"
    return ans2

s = input()
t = input()
print(solve(s,t))