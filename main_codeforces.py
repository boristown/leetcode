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
        self.n = len(s)
        self.s = s
        self.psum = [0]
        self.pbalance = [0]
        self.left = [0]*self.n  #The position of the first ')' to the left of s[i] (with i)
        self.right = [0]*self.n  #The position of the first '(' to the right of s[i] (with i)
        i2,j2 = 0,0
        p,sm=0,0
        j2 = -1
        for i,c in enumerate(s):
            if c==')':
                j2 = i
            self.left[i] = j2
        i2 = self.n
        for i in range(self.n-1,-1,-1):
            if s[i]=='(':
                i2 = i
            self.right[i] = i2
        for c in s:
            if c == '(':
                p+=1
            elif p>0:
                p-=1
                sm+=1
            self.psum.append(sm)
            self.pbalance.append(p)
        
    def get_range(self,i,j):
        '''
        correct bracket length in [i,j)
        '''
        i2,j2 = self.right[i],self.left[j-1]
        if i2 >= j2: return 0
        delta = self.pbalance[i2] - self.pbalance[j2+1]
        ans = self.psum[j2+1] - self.psum[i2]
        if delta > 0:
            ans -= delta
        return ans*2

s = input() #input string
n = int(input()) #input int
br = bracket_range(s)
for _ in range(n): #iter for test cases
    i,j = map(int,input().split()) #input tuple
    print(br.get_range(i-1,j))