#begin of leetcode template
from collections import *
import heapq
import itertools
from functools import *
import math
import bisect
from heapq import *

class Solution:
    def kSum(self, nums, k: int) -> int:
        sm = 0
        for i, x in enumerate(nums):
            #计算正数和
            if x >= 0: sm += x
            #将负数转化为正数
            else: nums[i] = -x
        #将绝对值排序
        nums.sort()
        hp = [(0, 0)]  # 取负号变成最大堆
        while k > 1:
            k -= 1
            #贪心：每次弹出最大和，减去最小绝对值得到下一个答案
            s, i = heappop(hp)
            if i < len(nums):
                heappush(hp, (s + nums[i], i + 1))  # 保留 nums[i-1]
                if i: heappush(hp, (s + nums[i] - nums[i - 1], i + 1))  # 不保留 nums[i-1]
        return sm-hp[0][0] #和 - 第k个最小子序列和

if __name__ == "__main__":
    slt = Solution()
    print(slt.kSum([2,4,-2],5))
    print(slt.kSum([1,-2,3,4,-10,12],16))