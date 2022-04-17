from collections import *
class TopologicalSortor:
    '''
    拓扑排序器
    '''
    def __init__(self,vertices): 
        self.graph = defaultdict(set)
        self.V = vertices
    
    def detectCircle(self,u):
        self.detectedNode.add(u)
        for v in self.graph[u]:
            if v not in self.pathNode:
                self.pathNode.add(v)
                self.detectCircle(v)
                self.pathNode.remove(v)
                if self.findCircle:
                    return
            else:
                self.findCircle = True
                return

    def addEdge(self,u,v):
        '''
        添加路径
        '''
        if v not in self.graph[u]:
            self.graph[u].add(v)
    
    def hasCircle(self):
        '''
        环路检测器
        '''
        self.pathNode = set()
        self.detectedNode = set()
        for i in range(self.V):
            if i not in self.detectedNode:
                self.findCircle = False
                self.pathNode.add(i)
                self.detectCircle(i)
                self.pathNode.remove(i)
                if self.findCircle: return True
        return False
  
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