#begin of leetcode template
from collections import *
import heapq
import itertools
from functools import *
import math
#end of leetcode template
inf = float("inf")
class Solution:
    def totalSteps(self, A) -> int:
        ans = 0
        B,n = [(-1,-inf)],len(A)
        for i,a in enumerate(A):
            if a>=B[-1][1]:
                B.append((i,a))
        n = len(B)-1
        for i in range(n):
            a,b = B[i][0],B[i+1][0]
            m = 1
            for j in range(a+1,b):
                if A[j]<=A[j+1]:
                    m+=1
                else:
                    m=1

if __name__ == "__main__":
    slt = Solution()
    print(slt.totalSteps([5,3,4,4,7,3,6,11,8,5,11])) #3
    print(slt.totalSteps([4,5,7,7,13])) #0
    print(slt.totalSteps([10,1,2,3,4,5,6,1,2,3])) #6
    print(slt.totalSteps([7,14,4,14,13,2,6,13])) #3
    print(100000002/50000001 == 2)
