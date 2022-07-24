#begin of leetcode template
from collections import *
import heapq
import itertools
from functools import *
import math
#end of leetcode template
MOD = 10**9 + 7
class Solution:
    def solve(self, n,mv):
        if mv == 0: return 0
        if n == 0: return 1
        if mv == 1: return 1
        if n == 1: return mv
        ans = 0
        for i in range(1,mv+1):
            ans = (ans + self.solve(n-1,mv//i)) % MOD
        return ans % MOD

    def idealArrays(self, n: int, mv: int) -> int:
        return self.solve(n,mv)

if __name__ == "__main__":
    slt = Solution()
    print(slt.idealArrays(1,5))
    #print(slt.idealArrays(5878,2900))