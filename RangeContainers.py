#https://github.com/boristown/leetcode/blob/main/RangeContainers.py
#用于处理Range的容器
#支持添加Range，减去Range，判断区间是否被包含，全局计数
import bisect

class RangeContainers(object):
    def __init__(self):
        self.range = []
        self.cnt = 0

    def addRange(self, left: int, right: int) -> None:
        '''
        添加Range：[left,right)
        时间复杂度：O(k)
        '''
        first = bisect.bisect_left(self.range, left, key=lambda r: r[1])
        last = bisect.bisect_right(self.range, right, key=lambda r: r[0]) # not included
        if first < last:
            left = min(left, self.range[first][0])
            right = max(right, self.range[last-1][1])
            #排除区间集[first,last)之间的计数
            for idx in range(first,last):
                self.cnt -= self.range[idx][1] - self.range[idx][0] 
            self.range = self.range[:first] + [[left, right]] + self.range[last:]
        else:
            self.range.insert(first, [left, right])
        #增加区间[left, right)的计数
        self.cnt += right-left

    def queryRange(self, left: int, right: int) -> bool:
        '''
        查询Range：[left,right)是否被包含
        时间复杂度：O(log k)
        '''
        idx = bisect.bisect_right(self.range, left, key=lambda r: r[0]) - 1
        return 0 <= idx < len(self.range) and self.range[idx][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        '''
        删除Range：[left,right)
        时间复杂度：O(k)
        '''
        first = bisect.bisect_right(self.range, left, key=lambda r: r[1])
        last = bisect.bisect_left(self.range, right, key=lambda r: r[0]) # not included
        if first < last:
            R = []
            if self.range[first][0] < left:
                R.append([self.range[first][0], left])
            if self.range[last-1][1] > right:
                R.append([right, self.range[last-1][1]])
            #排除区间集[first,last)之间的计数
            for idx in range(first,last):
                self.cnt -= self.range[idx][1] - self.range[idx][0] 
            self.range = self.range[:first] + R + self.range[last:]
            #新增R集合中的计数
            for r_left,r_right in R:
                self.cnt += r_right-r_left

    def count(self) -> int:
        '''
        区间全局计数
        时间复杂度：O(1)
        '''
        return self.cnt