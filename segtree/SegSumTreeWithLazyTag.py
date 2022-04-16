# 线段树的节点类
class TreeNode(object):
    '''
    线段树（区间和+区间增量更新)
    适用场景：区间更新
    '''
    def __init__(self):
        self.left = -1
        self.right = -1
        self.sum_num = 0
        self.lazy_tag = 0

    # 打印函数
    def __str__(self):
        return '[%s,%s,%s,%s]' % (self.left, self.right, self.sum_num, self.lazy_tag)

    # 打印函数
    def __repr__(self):
        return '[%s,%s,%s,%s]' % (self.left, self.right, self.sum_num, self.lazy_tag)


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
            self.tree[index].sum_num = self.arr[left - 1]
        else:
            mid = (left + right) // 2
            self._build(index * 2, left, mid)
            self._build(index * 2 + 1, mid + 1, right)
            self.pushup_sum(index)

    # 构建线段树
    def build(self):
        self._build(1, 1, self.n)

    def _update2(self, ql, qr, val, i, l, r, ):
        mid = (l + r) // 2
        if l >= ql and r <= qr:
            self.tree[i].sum_num += (r - l + 1) * val  # 更新和
            self.tree[i].lazy_tag += val  # 更新懒惰标记
        else:
            self.pushdown_sum(i)
            if mid >= ql:
                self._update2(ql, qr, val, i * 2, l, mid)
            if qr > mid:
                self._update2(ql, qr, val, i * 2 + 1, mid + 1, r)
            self.pushup_sum(i)

    # 区间修改(坐标从1开始，val为增量)
    def update2(self, ql, qr, val, ):
        self._update2(ql, qr, val, 1, 1, self.n)

    def _query2(self, ql, qr, i, l, r, ):
        if l >= ql and r <= qr:  # 若当前范围包含于要查询的范围
            return self.tree[i].sum_num
        else:
            self.pushdown_sum(i)  # modify
            mid = (l + r) // 2
            res_l = 0
            res_r = 0
            if ql <= mid:  # 左子树最大的值大于了查询范围最小的值-->左子树和需要查询的区间交集非空
                res_l = self._query2(ql, qr, i * 2, l, mid, )
            if qr > mid:  # 右子树最小的值小于了查询范围最大的值-->右子树和需要查询的区间交集非空
                res_r = self._query2(ql, qr, i * 2 + 1, mid + 1, r, )
            return res_l + res_r

    # 区间查询(区间[ql-1,qr-1])
    def query2(self, ql, qr):
        return self._query2(ql, qr, 1, 1, self.n)

    # 求和,向上更新
    def pushup_sum(self, k):
        self.tree[k].sum_num = self.tree[k * 2].sum_num + self.tree[k * 2 + 1].sum_num

    # 向下更新lazy_tag
    def pushdown_sum(self, i):
        lazy_tag = self.tree[i].lazy_tag
        if lazy_tag != 0:  # 如果有lazy_tag
            self.tree[i * 2].lazy_tag += lazy_tag  # 左子树加上lazy_tag
            self.tree[i * 2].sum_num += (self.tree[i * 2].right - self.tree[i * 2].left + 1) * lazy_tag  # 左子树更新和
            self.tree[i * 2 + 1].lazy_tag += lazy_tag  # 右子树加上lazy_tag
            self.tree[i * 2 + 1].sum_num += (self.tree[i * 2 + 1].right - self.tree[
                i * 2 + 1].left + 1) * lazy_tag  # 右子树更新和
            self.tree[i].lazy_tag = 0  # 将lazy_tag 归0

    # 深度遍历
    def _show_arr(self, i):
        if self.tree[i].left == self.tree[i].right and self.tree[i].left != -1:
            print(self.tree[i].sum_num, end=" ")
        if 2 * i < len(self.tree):
            self._show_arr(i * 2)
            self._show_arr(i * 2 + 1)

    # 显示更新后的数组的样子
    def show_arr(self, ):
        self._show_arr(1)

    def __str__(self):
        return str(self.tree)

# 落谷测试用例1
def test():
    n = 5  # 1 5 4 2 3
    arr = [1, 5, 4, 2, 3]
    tree = Tree(n, arr)
    tree.build()
    tree.update2(2, 4, 2)
    # # print(tree)
    res = tree.query2(3, 3)
    # print(tree)
    print(res)
    tree.update2(1, 5, -1)
    tree.update2(3, 5, 7)
    res = tree.query2(4, 4)
    print(res)


if __name__ == '__main__':
    # 样例输出
    line1 = [int(x) for x in input().strip().split(" ")]
    n = line1[0]  # 数字的个数
    m = line1[1]  # 操作的个数
    arr = [int(x) for x in input().strip().split(" ")]
    tree = Tree(n, arr)
    tree.build()
    for i in range(m):
        line = [int(x) for x in input().split(" ")]
        op = line[0]
        if op == 1:
            tree.update2(line[1], line[2], line[3])
        elif op == 2:
            res = tree.query2(line[1], line[1])
            print(res)

