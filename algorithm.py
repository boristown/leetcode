def prefix2D(matrix):
    '''
    二维前缀和
    '''
    if not matrix: return matrix
    height=len(matrix)
    width=len(matrix[0])
    prefix=[[0] * (width+1) for _ in range(height+1)]
    for i in range(1,height+1):
        for j in range(1,width+1):
            prefix[i][j]=prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+matrix[i-1][j-1]
    return prefix

def LCS(text1: str, text2: str) -> int:
    """
    最长公共子序列
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

def largestRectangleArea(heights) -> int:
    '''
    剑指 Offer II 039. 直方图最大矩形面积
    '''
    stack=[(-1,-1)]
    heights.append(0)
    ans=0
    for i,h in enumerate(heights):
        while stack[-1][1]>h:
            _,oh = stack.pop()
            s=(i-stack[-1][0]-1)*oh
            ans=max(ans,s)
        stack.append((i,h))
    return ans