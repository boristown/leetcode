def TSP(graph):
    '''
    旅行商问题:状压DP
    在一个图中，从某个点出发将所有点恰好遍历一遍，使得最后路过的路径的总权值最大
    graph：有向带权图graph[i][j]表示从i到j的权值
    返回值：最大权值，最优路径
    '''
    N=len(graph)
    # dp[mask][i] = most overlap with mask, ending with ith element
    dp = [[0] * N for _ in range(1<<N)]
    parent = [[None] * N for _ in range(1<<N)]
    for mask in range(1, 1 << N):
        for bit in range(N):
            if (mask >> bit) & 1:
                # Let's try to find dp[mask][bit].  Previously, we had
                # a collection of items represented by pmask.
                pmask = mask ^ (1 << bit)
                if pmask == 0: continue
                for i in range(N):
                    if (pmask >> i) & 1:
                        # For each bit i in pmask, calculate the value
                        # if we ended with word i, then added word 'bit'.
                        value = dp[pmask][i] + graph[i][bit]
                        if value > dp[mask][bit]:
                            dp[mask][bit] = value
                            parent[mask][bit] = i

    # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
    # Reconstruct answer:

    # Follow parents down backwards path that retains maximum overlap
    ans = []
    mask = (1<<N) - 1
    i = max(range(N), key = dp[-1].__getitem__)
    max_weight = dp[-1][i]

    while i is not None:
        ans.append(i)
        mask, i = mask ^ (1<<i), parent[mask][i]

    # Reverse path to get forwards direction; add all remaining words
    ans = ans[::-1]
    seen = [False] * N
    for x in ans:
        seen[x] = True
    ans.extend([i for i in range(N) if not seen[i]])
    return max_weight,ans
