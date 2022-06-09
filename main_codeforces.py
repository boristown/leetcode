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
from functools import reduce
from collections import *

class SegTree:
    def __init__(self, f1, f2, l, r, v = 0):
        self.default = v
        self.ans = f2(v,r-l)
        self.f1 = f1
        self.f2 = f2
        self.l = l #left
        self.r = r #right
        self.v = v #init value
        self.lazy_tag = 0 #Lazy tag
        self.left = None #SubTree(left,bottom)
        self.right = None #SubTree(right,bottom)
    
    @property
    def mid_h(self):
        return (self.l + self.r) // 2

    def create_subtrees(self):
        midh = self.mid_h
        if not self.left and midh > self.l:
            self.left = SegTree(self.f1, self.f2, self.l, midh, self.default)
        if not self.right:
            self.right = SegTree(self.f1, self.f2, midh, self.r, self.default)

    def init_seg(self, M):
        m0 = M[0]
        self.lazy_tag = 0
        for a in M:
            if a!=m0:
                break
        else:
            self.v = m0
            self.ans = self.f2(m0,len(M))
            return self.ans
        self.v = '#'
        midh = self.mid_h
        self.create_subtrees()
        self.ans = self.f1(self.left.init_seg(M[:midh-self.l]), self.right.init_seg(M[midh-self.l:]))
        return self.ans
    
    def cover_seg(self, l, r, v):
        if self.v == v or l >= self.r or r <= self.l:
            return self.ans
        if l <= self.l and r >= self.r:
            self.v = v
            self.lazy_tag = 0
            self.ans = self.f2(v,self.r-self.l)
            return self.ans
        self.create_subtrees()
        if self.v != '#':
            if self.left:
                self.left.v = self.v
                self.left.ans = self.f2(self.v,self.left.r-self.left.l)
            if self.right:
                self.right.v = self.v
                self.right.ans = self.f2(self.v,self.right.r-self.right.l)
            self.v = '#'
        #push up
        self.ans = self.f1(self.left.cover_seg(l, r, v),self.right.cover_seg(l, r, v))
        return self.ans

    def inc_seg(self, l, r, v):
        if v == 0 or l >= self.r or r <= self.l:
            return self.ans
        #self.ans = '?'
        if l <= self.l and r >= self.r:
            if self.v == '#':
                self.lazy_tag += v
            else:
                self.v += v
            self.ans += self.f2(v,self.r-self.l)
            return self.ans
        self.create_subtrees()
        if self.v != '#':
            self.left.v = self.v
            self.left.ans = self.f2(self.v,self.left.r-self.left.l)
            self.right.v = self.v
            self.right.ans = self.f2(self.v,self.right.r-self.right.l)
            self.v = '#'
        self.pushdown()
        self.ans = self.f1(self.left.inc_seg(l, r, v),self.right.inc_seg(l, r, v))
        return self.ans

    def inc_idx(self, idx, v):
        if v == 0 or idx >= self.r or idx < self.l:
            return self.ans
        if idx == self.l == self.r - 1:
            self.v += v
            self.ans += self.f2(v,1)
            return self.ans
        self.create_subtrees()
        if self.v != '#':
            self.left.v = self.v
            self.left.ans = self.f2(self.v,self.left.r-self.left.l)
            self.right.v = self.v
            self.right.ans = self.f2(self.v,self.right.r-self.right.l)
            self.v = '#'
        self.pushdown()
        self.ans = self.f1(self.left.inc_idx(idx, v),self.right.inc_idx(idx, v))
        return self.ans

    def pushdown(self):
        if self.lazy_tag != 0:
            if self.left:
                if self.left.v != '#':
                    self.left.v += self.lazy_tag
                    self.left.lazy_tag = 0
                else:
                    self.left.lazy_tag += self.lazy_tag
                self.left.ans += self.f2(self.lazy_tag, self.left.r-self.left.l)
            if self.right:
                if self.right.v != '#':
                    self.right.v += self.lazy_tag
                    self.right.lazy_tag = 0
                else:
                    self.right.lazy_tag += self.lazy_tag
                self.right.ans += self.f2(self.lazy_tag, self.right.r-self.right.l)
            self.lazy_tag = 0

    def query(self, l, r):
        if l>=r: return 0
        if l <= self.l and r >= self.r:
            return self.ans
        if self.v != '#':
            return self.f2(self.v, min(self.r, r) - max(self.l, l))
        midh = self.mid_h
        anss = []
        if l < midh:
            anss.append(self.left.query(l, r))
        if r > midh:
            anss.append(self.right.query(l, r))
        return reduce(self.f1,anss)

n,t = map(int,input().split()) #input tuple
L = list(map(int,input().split()))
def f1(a,b):
    c1,x1 = a
    c2,x2 = b
    C = set()
    for c in c1:
        if c in c2:
            C.add(c)
    return c1+c2,x1+x2+2*sum(c*c1[c]*c2[c] for c in C)

def f2(a,n):
    ans = 0
    c1,x1 = a
    c2 = Counter()
    for c in c1:
        c2[c] = c1[c]*n
        ans += (c2[c]**2) * c
    return c2,ans

ST = set()
Q = []
M = {}
for q in range(t):
    i,j = map(int,input().split()) #input tuple
    Q.append([i,j])
    ST.add(i-1)
    ST.add(j)

SL = sorted(list(ST))
for i,a in enumerate(SL):
    M[a] = i

MAX = len(SL)
Evt = []
i = 0
cnt = Counter()
ans = 0
for idx in SL:
    while idx > i:
        a = L[i]
        cnt[a]+=1
        i+=1
    #for a in cnt:
    #    ans += a * (cnt[a]**2)
    #Evt.append((cnt,ans))
    Evt.append(Counter(cnt))
    #ans = 0
    #cnt = Counter()

def calc(cnt):
    ans = 0
    for a in cnt:
        ans += a * (cnt[a]**2)
    return ans

#seg = SegTree(f1,f2,0,MAX-1,(Counter({0:1}),0))
#seg.init_seg(Evt)
for i,j in Q: #iter for test cases
    #ans = seg.query(M[i-1],M[j])[1]
    ans = Evt[M[j]] - Evt[M[i-1]]
    print(calc(ans))