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
class BoolSearch:
    @staticmethod
    def right(l,r,func,param=None):
        if param:
            while l<r:
                mid=(l+r)//2
                if func(mid,param):
                    r=mid
                else:
                    l=mid+1
            return r
        else:
            while l<r:
                mid=(l+r)//2
                if func(mid):
                    r=mid
                else:
                    l=mid+1
            return r

    @staticmethod
    def left(l,r,func,param=None):
        if param:
            while l<r:
                mid=(l+r)//2+1
                if func(mid,param):
                    l=mid
                else:
                    r=mid-1
            return l
        else:
            while l<r:
                mid=(l+r)//2+1
                if func(mid):
                    l=mid
                else:
                    r=mid-1
            return l

t=int(input())
for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    ans = 0
    side = 1 if A[0]>0 else -1
    mx = A[0]
    for a in A:
        side2 = 1 if a>0 else -1
        if side2 != side:
            ans += mx
            mx = a
            side = side2
        else:
            mx = max(mx,a)
    ans += mx
    print(ans)