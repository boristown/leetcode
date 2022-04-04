class SegMaxTree:
    '''
    线段树（区间最大值）
    '''
    def __init__(self, nums):
        n = len(nums)
        self.n = n
        self.seg = [0] * (n * 4)
        self.build(nums, 0, 0, n - 1)

    def build(self, nums, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = nums[s]
            return
        m = s + (e - s) // 2
        self.build(nums, node * 2 + 1, s, m)
        self.build(nums, node * 2 + 2, m + 1, e)
        self.seg[node] = max(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def change(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:
            self.change(index, val, node * 2 + 1, s, m)
        else:
            self.change(index, val, node * 2 + 2, m + 1, e)
        self.seg[node] = max(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def range(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:
            return self.seg[node]
        m = s + (e - s) // 2
        if right <= m:
            return self.range(left, right, node * 2 + 1, s, m)
        if left > m:
            return self.range(left, right, node * 2 + 2, m + 1, e)
        return max(self.range(left, m, node * 2 + 1, s, m), self.range(m + 1, right, node * 2 + 2, m + 1, e))

    def update(self, index: int, val: int) -> None:
        '''
        更新坐标index的值为val
        '''
        self.change(index, val, 0, 0, self.n - 1)

    def maxRange(self, left: int, right: int) -> int:
        '''
        求区间[left,right]的最大值
        '''
        return self.range(left, right, 0, 0, self.n - 1)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    st = SegMaxTree(arr)
    print(st.maxRange(1,5))
    st.update(5,4)
    print(st.maxRange(1,5))
    st.update(9,9)
    print(st.maxRange(7,9))
    st.update(9,100)
    print(st.maxRange(7,9))
    st.update(9,-100)
    st.update(8,-10)
    st.update(7,1)
    print(st.maxRange(6,9))
    print(st.maxRange(7,9))