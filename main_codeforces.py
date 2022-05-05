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

def solve(n,k,s):
    ans = []
    mx = ""
    s1 = "a"
    s2 = ""
    for c in s:
        if c > mx:
            mx  = c
            co = ord(c) - ord('a')
            if co > k:
                s2 = c
                break
            else:
                s1 = c
    M = {}
    for i in range(26):
        c = chr(ord('a')+i)
        M[c] = c
    #s1->a
    d = ord(s1)-ord('a')
    k-=d
    for i in range(d):
        M[chr(ord(s1)-i)] = 'a'
    #s2->?
    if s2:
        t = chr(ord(s2) - k)
        for i in range(k):
            M[chr(ord(s2)-i)] = t
    for c in s:
        ans.append(M[c])
    return "".join(ans)

t = int(input())
for _ in range(t): #iter for test cases
    n,k = map(int,input().split()) #input tuple
    s = input() #input string
    ans = solve(n,k,s)
    print(ans)