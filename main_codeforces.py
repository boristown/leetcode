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
import math

inf = float("inf")

def get_primes(n=100000):
    flag = False
    prime_number = [2]
    for i in range(3, n, 2):
        edge = math.ceil(math.sqrt(i))+1
        for j in prime_number:
            if i % j == 0:
                flag = True
                break
            if j >= edge:
                flag = False
                break
        if not flag:
            prime_number.append(i)
    return prime_number

n = int(input())
if n == 1:
    print(1)
    print(1)
elif n == 2:
    print(1)
    print(1,1)
else:
    primes = set(get_primes(n+1))
    print(2)
    ans = []
    for i in range(2,n+2):
        ans.append("1" if i in primes else "2")
    print(" ".join(ans))