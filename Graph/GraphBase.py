from collections import *

class GraphBase:
    '''
    图论工具类
    适用范围：图论相关问题
    '''
    @staticmethod
    def matrix2graph(grid) -> dict:
        '''
        邻接矩阵转无向图
        '''
        graph = {}
        n = len(grid)
        for i in range(n-1):
            for j in range(i+1,n):
                if grid[i][j]:
                    if i not in graph:
                        graph[i] = set()
                    if j not in graph:
                        graph[j] = set()
                    graph[i].add(j)
                    graph[j].add(i)
        return graph

    @staticmethod
    def maze2graph(grid) -> dict:
        '''
        二维迷宫转无向图
        param grid:二维矩阵，1是有效区域，0是无效区域
        时间：O(m*n)
        空间：O(m*n)
        '''
        m=len(grid)
        n=len(grid[0])
        num=m*n
        nab = [(0,1),(0,-1),(1,0),(-1,0)]
        graph = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    idx = i*n+j
                    graph[idx] = set()
                    for a,b in nab:
                        i2,j2=i+a,j+b
                        if 0<=i2<m and 0<=j2<n and grid[i2][j2]:
                            idx2 = i2*n+j2
                            graph[idx].add(idx2)
        return graph
