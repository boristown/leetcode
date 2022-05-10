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

def solve(n,L,s):
    leaf = []
    st = set()
    for i in L:
        st.add(i)
    CW,CB = Counter(),Counter()
    for node in range(1,n+1):
        if node not in st:
            leaf.append(node)
            if s[node-1] == 'W':
                CW[node],CB[node] = 1,0
            else:
                CW[node],CB[node] = 0,1
    vis = set()
    for lf in leaf:
        a = lf
        k1,k2 = CW[lf],CB[lf]
        while a>=2:
            p = L[a-2]
            if p not in vis:
                vis.add(p)
                if s[p-1] == 'W':
                    CW[p],CB[p] = 1,0
                else:
                    CW[p],CB[p] = 0,1
            CW[p]+=k1
            CB[p]+=k2
            a = p
    ans = 0
    for node in range(1,n+1):
        if CB[node] == CW[node]:
            ans+=1
    return ans

t = int(input())
for _ in range(t): #iter for test cases
    n = int(input()) #input int
    L = list(map(int,input().split())) #input list
    s = input() #input string
    ans = solve(n,L,s)
    print(ans)