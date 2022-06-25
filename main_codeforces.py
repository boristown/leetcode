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

t = int(input()) #input number of test cases
for _ in range(t):
    n = int(input()) #input number of test cases
    s = input()
    a = ""
    b = ""
    f = 0
    for c in s:
        if c == '2':
            if not f:
                a+="1"
                b+="1"
            else:
                a+='0'
                b+='2'
        elif c == '0':
            a+="0"
            b+="0"
        else:
            if not f:
                a+="1"
                b+="0"
            else:
                a+="0"
                b+="1"
            f = 1
    print(a)
    print(b)