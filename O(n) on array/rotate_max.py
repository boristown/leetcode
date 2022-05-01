def rotate_max_F(L):
    '''
    计算将序列L向右旋转k(0<=k<n-1)后，函数F的最大值
    F(k) = 0 * Lk[0] + 1 * Lk[1] + ... + (n - 1) * Lk[n - 1]
    时间复杂度：O(n)
    '''
    #分析：
    #F(0) = 0 * L[0] + 1 * L[1] + ... + (n - 1) * L[n - 1]
    #F(1) = 0 * L[n - 1]  + 1 * L[0] + ... + (n - 1) + L[n - 2]
    #F(2) = 0 * L[n - 2]  + 1 * L[n - 1] + ... + (n - 1) + L[n - 3]
    #做差：
    #F(1) - F(0) = L[0] + L[1] + …… + L[n-2] - (n-1) * L[n-1] = sum(L) - L[n-1] * n
    #F(2) - F(1) = L[0] + L[1] + …… + L[n-3] - (n-1) * L[n-2] + L[n-1] = sum(L) - L[n-2] * n
    #F(3) - F(2) = sum(L) - L[n-3]*n
    #F(k) - F(k-1) = sum(L) - L[n-k]*n
    #过程：
    #1 计算n
    n = len(L)
    #2 计算sum(L)
    sumL = sum(L)
    #3 计算F(0)
    f = 0
    for i in range(n):
        f += L[i]*i
    #4 计算F(1)到F(n-1)并统计最大值
    ans = f
    for k in range(1,n):
        f += sumL - L[n-k]*n
        ans = max(ans,f)
    #5 输出最大值
    return ans