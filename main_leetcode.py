#begin of leetcode template
from collections import *
import heapq
import itertools
from functools import *
import math
import bisect

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        M = [ord(c)-ord('a') for c in s]
        n = len(s)
        @cache
        def dp(i):
            ans = 1
            for j in range(i+1,n):
                if abs(M[j] - M[i])<=k:
                    ans = max(ans,1+dp(j))
            return ans
        return max(dp(i) for i in range(n))

if __name__ == "__main__":
    slt = Solution()
    print(slt.longestIdealString("acfgbd",2)) #4
    print(slt.longestIdealString("abcd",3)) #4
    print(slt.longestIdealString("lkpkxcigcs",6)) #7
    print(slt.longestIdealString("pvjcci",4)) #2