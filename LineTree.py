# 线段树的节点类
class LineTreeNode(object):
    def __init__(self):
        self.left = -1
        self.right = -1
        self.sum_num = 0

    # 打印函数
    def __str__(self):
        return '[%s,%s,%s]' % (self.left, self.right, self.sum_num)

    # 打印函数
    def __repr__(self):
        return '[%s,%s,%s]' % (self.left, self.right, self.sum_num)

# 线段树类
# 以_开头的是递归实现
class LineTree(object):
    def __init__(self, n, arr):
        self.n = n
        self.max_size = 4 * n
        self.tree = [LineTreeNode() for i in range(self.max_size)]  # 维护一个TreeNode数组
        self.arr = arr

    # index从1开始
    def _build(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right
        if left == right:
            self.tree[index].sum_num = self.arr[left - 1]
        else:
            mid = (left + right) // 2
            self._build(index * 2, left, mid)
            self._build(index * 2 + 1, mid + 1, right)
            self.pushup_sum(index)

    # 构建线段树
    def build(self):
        self._build(1, 1, self.n)

    def _update(self, point, val, i, l, r, ):
        if self.tree[i].left == self.tree[i].right:
            self.tree[i].sum_num += val
        else:
            mid = (l + r) // 2
            if point <= mid:
                self._update(point, val, i * 2, l, mid)
            else:
                self._update(point, val, i * 2 + 1, mid + 1, r)
                # 根据左右子树更新当前的值
            self.pushup_sum(i)

    # 单点更新
    # point 要更新的数在数组的下标 val更新的值
    def update(self, point, val, ):
        self._update(point, val, 1, 1, self.n)

    # 求和
    def pushup_sum(self, k):
        self.tree[k].sum_num = self.tree[k * 2].sum_num + self.tree[k * 2 + 1].sum_num

    def _query(self, ql, qr, i, l, r, ):
        if l >= ql and r <= qr:  # 若当前范围包含于要查询的范围
            return self.tree[i].sum_num
        else:
            mid = (l + r) // 2
            res_l = 0
            res_r = 0
            if ql <= mid:  # 左子树最大的值大于了查询范围最小的值-->左子树和需要查询的区间交集非空
                res_l = self._query(ql, qr, i * 2, l, mid, )
            if qr > mid:  # 右子树最小的值小于了查询范围最大的值-->右子树和需要查询的区间交集非空
                res_r = self._query(ql, qr, i * 2 + 1, mid + 1, r, )
            return res_l + res_r

    # 区间查询
    def query(self, ql, qr):
        return self._query(ql, qr, 1, 1, self.n)

    # 深度遍历打印数组
    def _show_arr(self, i):
        if self.tree[i].left == self.tree[i].right and self.tree[i].left != -1:
            print(self.tree[i].sum_num, end=" ")
        if 2 * i < len(self.tree):
            self._show_arr(i * 2)
            self._show_arr(i * 2 + 1)

    # 显示更新后的数组的样子
    def show_arr(self, ):
        self._show_arr(1)