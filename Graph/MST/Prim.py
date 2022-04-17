#最小生成树（Minimum Spanning Tree，MST）
#我们定义无向连通图的 最小生成树（Minimum Spanning Tree，MST）为边权和最小的生成树。
#https://blog.csdn.net/weixin_44193909/article/details/88894487
#Prim algorithm(python)
from collections import defaultdict
from heapq import heapify, heappush, heappop
import time
start = time.perf_counter()
def Prim(nodes, edges):
    '''  基于最小堆实现的Prim算法  '''
    element = defaultdict(list)
    for start, stop, weight in edges:
        element[start].append((weight, start, stop))
        element[stop].append((weight, stop, start))
    all_nodes = set(nodes)
    used_nodes = set(nodes[0])
    usable_edges = element[nodes[0]][:]
    heapify(usable_edges)
    # 建立最小堆
    MST = []
    while usable_edges and (all_nodes - used_nodes):
        weight, start, stop = heappop(usable_edges)
        if stop not in used_nodes:
            used_nodes.add(stop)
            MST.append((start, stop, weight))
            for member in element[stop]:
                if member[2] not in used_nodes:
                    heappush(usable_edges, member)

    return MST

def main():
    nodes = list('123456789')
    edges = [("1", "2", 5), ("1", "3",13),("1", "4",12), ("1", "5",10),
                   ("1", "6", 8), ("1", "7", 6),("1", "8", 2), ("1", "9", 5),
                   ("2", "3", 3), ("2", "9", 1),("3", "4", 9), ("4", "5",11),
                   ("5", "6", 9), ("6", "7", 6),("7", "8", 7), ("8", "9", 4)]
    print("\n\nThe undirected graph is :", edges)
    print("\n\nThe minimum spanning tree by Prim is : ")
    print(Prim(nodes, edges))

if __name__ == '__main__':
    main()
end = time.perf_counter()
print('Running time: %f seconds'%(end-start))

'''
The undirected graph is : [('1', '2', 5), ('1', '3', 13), ('1', '4', 12), ('1', '5', 10), ('1', '6', 8), ('1', '7', 6), ('1', '8', 2), ('1', '9', 5), ('2', '3', 3), ('2', '9', 1), ('3', '4', 9), ('4', '5', 11), ('5', '6', 9), ('6', '7', 6), ('7', '8', 7), ('8', '9', 4)]
The minimum spanning tree by Prim is :
[('1', '8', 2), ('8', '9', 4), ('9', '2', 1), ('2', '3', 3), ('1', '7', 6), ('7', '6', 6), ('3', '4', 9), ('6', '5', 9)]   
Running time: 0.001529 seconds
'''