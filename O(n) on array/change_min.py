def change_min_palindrome(s,que):
    '''
    # 在区间内更改最少的元素，使得它不包含长度2以上的回文
    # 输入包括一系列区间查询，输出变更区间的最小成本
    # 字符串只含有a,b,c 
    #https://codeforces.com/problemset/problem/1555/D
    #*1600
    #输入:
    s:字符串
    que:查询序列，每个查询为(l,r)表示区间范围，坐标从1开始
    #返回：
    ans:每个查询的答案
    '''
    #分析
    #由于不能包含长度2以上的回文，且只有三种字符
    #推测可能只存在不超过10种合理的排列方式
    #试着构造这样的排列：
    #长度1：a / b / c
    #长度2：ab / ac / ba / bc / ca / cb
    #长度3：abc / acb / bac / bca / cab / cba
    #长度4：abca / acba / bacb / bcab / cabc / cbac
    #长度5：abcab / acbac / bacba / bcabc / cabca / cbacb
    #可以看出对于大于1的每一种长度，都只存在6种合理的排列
    #1 暴力解法：
    # 对比区间与6种排列，分别计算成本
    # 每次查询的时间复杂度为O(n)
    # 总时间复杂度为O(m*n) 
    # 肯定超时
    #2 前缀优化：
    # 分别使用6种排列方式扫描原字符串
    # 并使用前缀pre[k][i]记录第k种排列方式扫描到第i个字符时的成本
    # 初始化时间复杂度：O(n)
    # 每次查询的时间复杂度：O(1)
    # 肯定通过
    pat = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    n = len(s)
    pre = [[0]*(n+1) for _ in range(6)]
    for k in range(6):
        for i in range(n):
            pre[k][i+1]=pre[k][i]
            if s[i] != pat[i%3]:
                pre[k][i+1]+=1
    ans = []
    for l,r in que:
        a = float("inf")
        for k in range(6):
            a = min(a,pre[k][r]-pre[k][l-1])
        ans.append(a)
    return ans