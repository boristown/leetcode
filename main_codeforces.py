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
class SegTreeLite:
    def __init__(self, n: int):
        self.n = n
        self.sum = [0] * (n * 4)

    def _add(self, o: int, l: int, r: int, idx: int, val: int):
        if l == r:
            self.sum[o] += val
            return
        m = (l + r) // 2
        if idx <= m: self._add(o * 2, l, m, idx, val)
        else: self._add(o * 2 + 1, m + 1, r, idx, val)
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]

    def _query_sum(self, o: int, l: int, r: int, L: int, R: int):
        if L <= l and r <= R: return self.sum[o]
        sum = 0
        m = (l + r) // 2
        if L <= m: sum += self._query_sum(o * 2, l, m, L, R)
        if R > m: sum += self._query_sum(o * 2 + 1, m + 1, r, L, R)
        return sum
    
    def query_sum(self, L: int, R: int):
        '''
        Query sum in range [l,r)
        '''
        return self._query_sum(1,1,self.n,L+1,R)
    
    def add(self, idx: int, val: int):
        '''
        Increase arr[idx] by val
        '''
        return self._add(1, 1, self.n, idx+1, val)

s = input() #input string
n = int(input()) #input int
Que = []
for q in range(n): #iter for test cases
    i,j = map(int,input().split()) #input tuple
    Que.append((j,i-1,q))
ns = len(s)
seg = SegTreeLite(ns)
st = []
n_ans = len(Que)
ans = [0]*n_ans
k = -1
for j,i,idx in sorted(Que,key=lambda x:x[0]):
    while j > k+1:
        k+=1
        a = s[k]
        if a == '(':
            st.append(k)
        else:
            if st:
                k2 = st.pop()
                seg.add(k2,2)
    ans[idx] = seg.query_sum(i,j)
for a in ans:
    print(a)