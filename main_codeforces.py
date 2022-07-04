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

from bisect import *
from collections import *

inf = float("inf")

def solve(n,m,A):
    cnt = Counter([a%m for a in A])
    ans = 1 if cnt[0] else 0
    n -= cnt[0]
    cnt[0] = 0
    for i in range(1,m):
        j = m-i
        if cnt[i] and cnt[j]:
            if i == j:
                n-=cnt[i]
                cnt[i]=0
            else:
                n1 = min(cnt[i],cnt[j])
                n2 = max(cnt[i],cnt[j])
                if n2>n1:
                    n3 = n1 + 1
                    n-=n1*2+1
                else:
                    n3 = n1
                    n-=n1*2
                cnt[i]-=n1
                cnt[j]-=n1
                if cnt[i] > 0:
                    cnt[i]-=1
                elif cnt[j] > 0:
                    cnt[j]-=1
            #print(i,j)
            ans += 1
        if cnt[i]:
            #print(i,"*",cnt[i])
            ans += cnt[i]
            n-=cnt[i]
            cnt[i] = 0
        if not n:
            break
    return ans

t = int(input())
for _ in range(t):
    n,m = map(int,input().split()) #input tuple
    A = list(map(int,input().split())) #input list
    ans = solve(n,m,A)
    print(ans)
