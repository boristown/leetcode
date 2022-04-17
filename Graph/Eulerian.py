from collections import *
class Eulerian:
    
    def findEulerian(self, tickets):
        '''
        寻找欧拉路（不必回到起点）
        Hierholzer 算法
        输入：[["start1","end1"],["start2","end2"],["end1","start2"]]
        输出: ["start1","end1","start2","end2"]
        '''
        def dfs(cur, graph, res):
            while graph[cur]: # 遍历所有边
                dfs(graph[cur].pop(), graph, res) # 访问并删除
            if not graph[cur]: # 将顶点入栈
                res.append(cur)
        #入度-1,出度+1
        ct = defaultdict(int)
        # 建图
        graph = defaultdict(list)
        #如果要找字典序最小的路径，就需要排序
        #for start, end in sorted(tickets)[::-1]:
        for start, end in tickets:
            graph[start].append(end)
            ct[start]+=1
            ct[end]-=1
        #找到出度大于入读的点作为起点
        mc = -1
        mv = None
        for v in ct:
            if ct[v]>mc:
                mc = ct[v]
                mv = v
        res = []
        dfs(mv, graph, res)
        return res[::-1] # 倒序输出