
from typing import List, Tuple
'''
Trajan算法求无向图的割点和桥
'''
class Tarjan:
    # 求无向连通图的桥
    @staticmethod
    def getCuttingPointAndCuttingEdge(edges: List[Tuple]):
        link, dfn, low = {}, {}, {}# link为字典邻接表
        global_time = [0]
        for a, b in edges:
            if a not in link:
                link[a] = []
            if b not in link:
                link[b] = []
            link[a].append(b)#无向图
            link[b].append(a)#无向图
            dfn[a], dfn[b] = 0x7fffffff, 0x7fffffff
            low[a], low[b] = 0x7fffffff, 0x7fffffff
 
 
        cutting_points, cutting_edges = [], []
 
        def dfs(cur, prev, root):
            global_time[0] += 1
            dfn[cur], low[cur] = global_time[0], global_time[0]
 
            children_cnt = 0
            flag = False
            for next in link[cur]:
                if next != prev:
                    if dfn[next] == 0x7fffffff:
                        children_cnt += 1
                        dfs(next, cur, root)
 
                        if cur != root and low[next] >= dfn[cur]:
                            flag = True
                        low[cur] = min(low[cur], low[next])
 
                        if low[next] > dfn[cur]:
                            cutting_edges.append([cur, next] if cur < next else [next, cur])
                    else:
                        low[cur] = min(low[cur], dfn[next])
 
            if flag or (cur == root and children_cnt >= 2):
                cutting_points.append(cur)
 
        dfs(edges[0][0], None, edges[0][0])
        return cutting_points, cutting_edges