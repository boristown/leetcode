#最小生成树（Minimum Spanning Tree，MST）
#我们定义无向连通图的 最小生成树（Minimum Spanning Tree，MST）为边权和最小的生成树。
# https://blog.csdn.net/johnjim0/article/details/109108875
#Kruskal算法
# 以全局变量X定义节点集合，即类似{'A':'A','B':'B','C':'C','D':'D'},如果A、B两点连通，则会更改为{'A':'B','B':'B",...},即任何两点连通之后，两点的值value将相同。
X = dict()
R = dict() # 各点的初始等级均为0,如果被做为连接的的末端，则增加1

def make_set(point):
    X[point] = point
    R[point] = 0
def find(point):
    if X[point] != point:
        X[point] = find(X[point])
    return X[point]
def merge(point1, point2):
    '''连接两个分量（节点）
    '''
    r1 = find(point1)
    r2 = find(point2)
    if r1 != r2:
        if R[r1] > R[r2]:
            X[r2] = r1
        else:
            X[r1] = r2
            if R[r1] == R[r2]:
                R[r2] += 1

def kruskal(vertices,edges):
    '''KRUSKAL算法实现
    '''
    for vertice in vertices:
        make_set(vertice)
    minu_tree = []
    edges.sort()  # 按照权重从小到大排序
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            merge(vertice1, vertice2)
            minu_tree.append(edge)
    return minu_tree


vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [(7, 'A', 'B'),
            (5, 'A', 'D'),
            (8, 'B', 'C'),
            (9, 'B', 'D'),
            (7, 'B', 'E'),
            (5, 'C', 'E'),
            (15, 'D', 'E'),
            (6, 'D', 'F'),
            (8, 'E', 'F'),
            (9, 'E', 'G'),
            (11, 'F', 'G'),
            ]
print(kruskal(vertices,edges))
#[(5, 'A', 'D'), (5, 'C', 'E'), (6, 'D', 'F'), (7, 'A', 'B'), (7, 'B', 'E'), (9, 'E', 'G')]