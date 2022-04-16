# 线段树的节点类
class TreeNode(object):
    '''
    线段树（区间增量更新+区间最大值)
    适用场景：区间更新
    '''
    def __init__(self):
        self.left = -1
        self.right = -1
        self.max_num = 0
        self.lazy_tag = 0

    # 打印函数
    def __str__(self):
        return '[%s,%s,%s,%s]' % (self.left, self.right, self.max_num, self.lazy_tag)

    # 打印函数
    def __repr__(self):
        return '[%s,%s,%s,%s]' % (self.left, self.right, self.max_num, self.lazy_tag)

# 线段树类
# 以_开头的是递归实现
class Tree(object):
    def __init__(self, n, arr):
        self.n = n
        self.max_size = 4 * n
        self.tree = [TreeNode() for i in range(self.max_size)]  # 维护一个TreeNode数组
        self.arr = arr

    # index从1开始
    def _build(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right
        if left == right:
            self.tree[index].max_num = self.arr[left - 1]
        else:
            mid = (left + right) // 2
            self._build(index * 2, left, mid)
            self._build(index * 2 + 1, mid + 1, right)
            self.pushup_max(index)

    # 构建线段树
    def build(self):
        self._build(1, 1, self.n)

    def _update2(self, ql, qr, val, i, l, r, ):
        mid = (l + r) // 2
        if ql <= l and r <= qr:
            self.tree[i].max_num += val  # 更新最大值
            self.tree[i].lazy_tag += val  # 更新懒惰标记
        else:
            self.pushdown_max(i)
            if mid >= ql:
                self._update2(ql, qr, val, i * 2, l, mid)
            if qr > mid:
                self._update2(ql, qr, val, i * 2 + 1, mid + 1, r)
            self.pushup_max(i)

    # 区间修改(坐标从1开始，val为增量)
    def update2(self, ql, qr, val, ):
        self._update2(ql, qr, val, 1, 1, self.n)

    def _query2(self, ql, qr, i, l, r, ):
        if ql <= l and r <= qr:  # 若当前范围包含于要查询的范围
            return self.tree[i].max_num
        else:
            self.pushdown_max(i)  # modify
            mid = (l + r) // 2
            res_l = 0
            res_r = 0
            if ql <= mid:  # 左子树最大的值大于了查询范围最小的值-->左子树和需要查询的区间交集非空
                res_l = self._query2(ql, qr, i * 2, l, mid, )
            if qr > mid:  # 右子树最小的值小于了查询范围最大的值-->右子树和需要查询的区间交集非空
                res_r = self._query2(ql, qr, i * 2 + 1, mid + 1, r, )
            return max(res_l,res_r)

    # 区间查询(区间[ql-1,qr-1])
    def query2(self, ql, qr):
        return self._query2(ql, qr, 1, 1, self.n)

    # 求和,向上更新
    def pushup_max(self, k):
        self.tree[k].max_num = max(self.tree[k * 2].max_num, self.tree[k * 2 + 1].max_num)

    # 向下更新lazy_tag
    def pushdown_max(self, i):
        lazy_tag = self.tree[i].lazy_tag
        if lazy_tag != 0:  # 如果有lazy_tag
            self.tree[i * 2].lazy_tag += lazy_tag  # 左子树加上lazy_tag
            self.tree[i * 2].max_num += lazy_tag  # 左子树更新最大值
            self.tree[i * 2 + 1].lazy_tag += lazy_tag  # 右子树加上lazy_tag
            self.tree[i * 2 + 1].max_num += lazy_tag  # 右子树更新最大值
            self.tree[i].lazy_tag = 0  # 将lazy_tag 归0

    # 深度遍历
    def _show_arr(self, i):
        if self.tree[i].left == self.tree[i].right and self.tree[i].left != -1:
            print(self.tree[i].max_num, end=" ")
        if 2 * i < len(self.tree):
            self._show_arr(i * 2)
            self._show_arr(i * 2 + 1)

    # 显示更新后的数组的样子
    def show_arr(self, ):
        self._show_arr(1)

    def __str__(self):
        return str(self.tree)

if __name__ == "__main__":
    #线段数初始化为[5,2,4,1,9]
    seg = Tree(5,[5,2,4,1,9])
    seg.build()
    #[3,3]最大值：1
    print(seg.query2(4,4))
    #[2,3]加1 [5,2,5,2,9]
    seg.update2(3,4,1)
    #[0,2]最大值：5
    print(seg.query2(1,3))
    #[1,3]加3 [5,5,8,5,9]
    seg.update2(2,4,3)
    #[2,4]最大值：9
    print(seg.query2(3,5))
    #[4,4]加2 [5,3,6,3,11]
    seg.update2(5,5,2)
    #[3,4]最大值：11
    print(seg.query2(4,5))