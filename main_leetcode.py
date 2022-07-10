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
        a=self.solve(2,mv)
        b=self.solve(3,mv)
        c=self.solve(4,mv)
        d1 = (b-a) - (a-mv)
        d2 = (c-b) - (b-a)
        ans = mv
        e = a-mv
        d = d1
        d3 = d2-d1
        for i in range(n-1):
            ans += e
            e+=d
            d+=d3
        return ans % MOD

if __name__ == "__main__":
    slt = Solution()
    print("5:")
    print(slt.idealArrays(1,5))
    print(slt.idealArrays(2,5))
    print(slt.idealArrays(3,5))
    print(slt.idealArrays(4,5))
    print(slt.idealArrays(5,5))
    print(slt.idealArrays(6,5))
    print(slt.idealArrays(7,5))
    print(slt.idealArrays(8,5))
    print(slt.idealArrays(9,5))
    print(slt.idealArrays(10,5))
    print(slt.idealArrays(11,5))
    print(slt.idealArrays(12,5))
    print("3:")
    print(slt.idealArrays(1,3))
    print(slt.idealArrays(2,3))
    print(slt.idealArrays(3,3))
    print(slt.idealArrays(4,3))
    print(slt.idealArrays(5,3))
    print("9:")
    print(slt.idealArrays(1,9))
    print(slt.idealArrays(2,9))
    print(slt.idealArrays(3,9))
    print(slt.idealArrays(4,9))
    print(slt.idealArrays(5,9))
    #print(slt.idealArrays(5878,2900))