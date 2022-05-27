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
        p1,p2,self.psum1,self.psum2 = 0,0,[0],[0]
        for a in s:
            if a == '(':
                p1+=1
            else:
                p2+=1
            self.psum1.append(p1)
            self.psum2.append(p2)
    
    def get_range(self,i,j):
        '''
        correct bracket length in [i,j)
        '''
        s1 = self.psum1[j]-self.psum1[i]
        s2 = self.psum2[j]-self.psum2[i]
        ans = min(s1,s2)
        return ans*2

s = input() #input string
n = int(input()) #input int
br = bracket_range(s)
for _ in range(n): #iter for test cases
    i,j = map(int,input().split()) #input tuple
    print(br.get_range(i-1,j))