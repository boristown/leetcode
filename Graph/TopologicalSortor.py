from graphlib import TopologicalSorter, CycleError

#注意：以下内容已作废
#请直接使用graphlib自带的拓扑排序器graphlib.TopologicalSorter
#示例代码：https://www.geeksforgeeks.org/topological-sorting-using-graphlib-python-module/

from collections import *
import collections

from typing import *

class TopologicalSortorNoCircle:
    '''
    拓扑排序器(无环图)
    '''
    def __init__(self,vertices): 
        self.graph = defaultdict(set)
        self.V = vertices

    def addEdge(self,u,v):
        '''
        添加路径
        '''
        if v not in self.graph[u]:
            self.graph[u].add(v)
    
    def topologicalSortUtil(self,v,visited,stack):
        visited[v] = True
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
        stack.insert(0,v)
  
    def topologicalSort(self):
        '''
        拓扑排序
        '''
        visited = [False]*self.V 
        stack =[] 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
        self.stack = stack
        return stack
    
    def is_Hamiltonian_path(self):
        '''
        拓扑排序的唯一性判断（哈密顿路径）
        '''
        for i in range(self.V - 1):
            a,b = self.stack[i],self.stack[i+1]
            if b not in self.graph[a]:
                return False
        return True

class CircleDetect:
    def noCircle(self, numCourses, prerequisites) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])
        
        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)
        
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        
        return valid

class TopologicalSortorWithCircle:
    def solve(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        带环路的拓扑排序器
        '''
        # 存储有向图
        edges = collections.defaultdict(list)
        # 存储每个节点的入度
        indeg = [0] * numCourses
        # 存储答案
        result = list()

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1
        
        # 将所有入度为 0 的节点放入队列中
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            # 从队首取出一个节点
            u = q.popleft()
            # 放入答案中
            result.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                # 如果相邻节点 v 的入度为 0，就可以选 v 对应的课程了
                if indeg[v] == 0:
                    q.append(v)

        if len(result) != numCourses:
            result = list()
        return result