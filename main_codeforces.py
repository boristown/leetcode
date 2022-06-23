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
from bisect import *
n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))
A.sort()
B.sort()
i=ans=0
j=-1
for a in A:
    l,r = bisect_left(B,a-1),bisect_right(B,a+1)-1
    if l < m:
        j2=max(j+1,l)
        if j2 > r or j2 >= m:
            continue
        j = j2
        ans+=1
    else:
        break
print(ans)