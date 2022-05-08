#begin of leetcode template
from collections import *
import heapq
import itertools
from functools import *
#end of leetcode template

MOD = 10**9+7

class Solution:
    def countTexts(self, P: str) -> int:
        M = [0,0,3,3,3,3,3,3,3,4]
        @cache
        def dp(m,n):
            if n==0:
                return 1
            ans = 0
            for i in range(1,min(m,n)+1):
                ans = (ans + dp(m,n-i)) % MOD
            #print("dp",m,n,ans)
            return ans
        cur = 0
        cnt = 0
        ans = 1
        for a in P:
            k = int(a)
            if k != cur:
                if cur != 0:
                    ans *= dp(M[cur],cnt) % MOD
                cur = k
                cnt = 1
            else:
                cnt+=1
        ans *= dp(M[cur],cnt) % MOD
        return ans

if __name__ == "__main__":
    slt = Solution()
    print(slt.countTexts("22233"))
    print(slt.countTexts("222222222222222222222222222222222222"))
    print(slt.countTexts("55555555999977779555"))