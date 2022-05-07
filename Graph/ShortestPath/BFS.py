from collections import * 
import random

def ShortestPathLen(graph,start,end):
    '''
    有向无权图中：从start到end的最短路长度
    '''
    if start == end: return 0
    Q = deque([(0,start)])
    vis = set([start])
    while Q:
        step,node = Q.popleft()
        step += 1
        for node2 in graph[node]:
            if node2 not in vis:
                vis.add(node2)
                if node2 == end:
                    return step
                Q.append((step,node2))
    return -1
    
def ShortestPath(graph,start,end):
    '''
    有向无权图中：从start到end的最短路
    '''
    if start == end: return [start]
    last = {}
    Q = deque([(0,start)])
    vis = set([start])
    ans = []
    while Q:
        step,node = Q.popleft()
        step += 1
        for node2 in graph[node]:
            if node2 not in vis:
                last[node2] = node
                vis.add(node2)
                if node2 == end:
                    ans.append(end)
                    while node2 in last:
                        ans.append(last[node2])
                        node2 = last[node2]
                    return ans[::-1]
                Q.append((step,node2))
    return ans[::-1]

def ShortestPathALL(graph,start):
    '''
    有向无权图中：从start到所有节点的最短路长度
    '''
    Q = deque([(0,start)])
    vis = set([start])
    ans = {start:0}
    while Q:
        step,node = Q.popleft()
        step += 1
        for node2 in graph[node]:
            if node2 not in vis:
                ans[node2] = step
                vis.add(node2)
                Q.append((step,node2))
    return ans

def ShortestPath_random(graph,start,end):
    '''
    有向无权图中：从start到end的随机最短路
    '''
    if start == end: return [start]
    last = {}
    Q = deque([(0,start)])
    vis = set([start])
    ans = []
    while Q:
        step,node = Q.popleft()
        step += 1
        random.shuffle(graph[node])
        for node2 in graph[node]:
            if node2 not in vis:
                last[node2] = node
                vis.add(node2)
                if node2 == end:
                    ans.append(end)
                    while node2 in last:
                        ans.append(last[node2])
                        node2 = last[node2]
                    return ans[::-1]
                Q.append((step,node2))
    return ans[::-1]