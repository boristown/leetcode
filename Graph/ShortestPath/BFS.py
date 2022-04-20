from collections import * 
def ShortestPathLen(graph,start,end):
    '''
    有向无权图中：从start到end的最短路长度
    '''
    if start == end: return 0
    Q = deque([(0,start)])
    vis = set(start)
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
    pass