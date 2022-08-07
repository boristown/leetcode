
def longestCycleTree(edges:list) -> int:
    '''
    寻找内向基环树中的最大环
    输入：
    edge[i]:返回节点i指向的下一个结点，-1表示没有下一个结点
    返回：
    最大环路长度
    '''
    time = [0] * len(edges)
    clock, ans = 1, -1
    for x, t in enumerate(time):
        if t: continue
        start_time = clock
        while x >= 0:
            if time[x]:  # 重复访问
                if time[x] >= start_time:  # 找到了一个新的环
                    ans = max(ans, clock - time[x])
                break
            time[x] = clock
            clock += 1
            x = edges[x]
    return ans