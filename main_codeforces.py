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

class bracket_range:
    def __init__(self,s):
        self.s = s
        self.psum = [0]
        p=0
        for c in s:
            if c == '(':
                p+=1
            self.psum.append(p)
        
    def get_range(self,i,j):
        '''
        correct bracket length in [i,j)
        '''
        ans = self.psum[i]
        for p in range(i,j):
            if self.s[p] == ')' and ans < self.psum[p+1]:
                ans += 1
        ans = (ans - self.psum[i])*2
        return ans

s = input() #input string
n = int(input()) #input int
br = bracket_range(s)
for _ in range(n): #iter for test cases
    i,j = map(int,input().split()) #input tuple
    print(br.get_range(i-1,j))