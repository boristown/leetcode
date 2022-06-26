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
for _ in range(t):
    s = input() #input string
    n = len(s)
    if n < 3:
        print(0)
    else:
        i,j = 0,2
        cnt = Counter(s[:3])
        ans = inf
        while cnt['1'] == 0 or cnt['2'] == 0 or cnt['3'] == 0:
            j+=1
            if j >= n: break
            cnt[s[j]]+=1
        if not (cnt['1'] == 0 or cnt['2'] == 0 or cnt['3'] == 0):
            ans = j-i+1
        if ans == inf:
            print(0)
        else:
            for i in range(1,n-2):
                cnt[s[i-1]]-=1
                while cnt['1'] == 0 or cnt['2'] == 0 or cnt['3'] == 0:
                    j+=1
                    if j >= n: break
                    cnt[s[j]]+=1
                if not (cnt['1'] == 0 or cnt['2'] == 0 or cnt['3'] == 0):
                    ans = min(ans,j-i+1)
            if ans == inf:
                print(0)
            else:
                print(ans)