from collections import *

def checktree_by_nabors(nabors):
    '''
    根据节点的上层或下层节点（不一定相邻）的集合，判断树的有效性
    nabors:包含节点上下级的集合字典
    返回:0 无效树;1 有效唯一树 2 有效不唯一树
    适用范围：树的有效性判断
    '''
    max_nabor = -float("inf")
    for a in nabors:
        nabors[a].add(a)
        if len(nabors[a]) > max_nabor:
            max_nabor = len(nabors[a])
            root = a
    if len(nabors) != max_nabor: return 0
    ans = 1
    for node in nabors:
        if node == root: continue
        cnt = len(nabors[node])
        nabor = nabors[node]
        minParentCnt = float("inf")
        minParentNabor = set()
        for nb in nabors[node]:
            if nb != node:
                parentcnt,parentnb = len(nabors[nb]),nabors[nb]
                if parentcnt >= cnt and parentcnt < minParentCnt:
                    minParentCnt = parentcnt
                    minParentNabor = parentnb
        if not nabor.issubset(minParentNabor): return 0
        if minParentCnt == cnt: ans = 2
    return ans