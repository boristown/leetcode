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

d,sumTime = map(int,input().split()) #input tuple
sum_min=sum_max=0
limit = []
for _ in range(d):
    l,r = map(int,input().split())
    limit.append((l,r))
    sum_min+=l
    sum_max+=r
if sumTime<sum_min or sumTime>sum_max:
    print("NO")
else:
    print("YES")
    ans = [l for l,r in limit]
    sm = sum_min
    i = 0
    while sm < sumTime:
        dis = limit[i][1] - ans[i]
        if dis + sm <= sumTime:
            ans[i] = limit[i][1]
            sm += dis
            i+=1
        else:
            delta = sumTime - sm
            ans[i] += delta
            break
    print(" ".join(map(str,ans)))