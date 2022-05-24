def min_range(arr, is_max=False):
    '''
    计算数组arr中每一个元素作为最小值的辐射范围
    输入：长度为n的整数数组arr
    is_max：计算最大值的辐射范围
    输出：长度为n的整数数组left和right
    left[i] 为左侧严格小于 arr[i] 的最近元素位置（不存在时为 -1）
    right[i] 为右侧小于等于 arr[i] 的最近元素位置（不存在时为 n）
    时间复杂度:O(n)
    '''
    n = len(arr)
    left, right, st = [-1] * n, [n] * n, []
    if is_max:
        for i, v in enumerate(arr):
            while st and arr[st[-1]] <= v: 
                right[st.pop()] = i
            if st: left[i] = st[-1]
            st.append(i)
    else:
        for i, v in enumerate(arr):
            while st and arr[st[-1]] >= v: 
                right[st.pop()] = i
            if st: left[i] = st[-1]
            st.append(i)
    return left, right