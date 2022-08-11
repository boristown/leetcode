#begin of codeforces template
# (don't delete):
#  
# from collections import *
# from heapq import *
# import bisect
#
#t = int(input()) #input number of test cases
#for _ in range(t): #iter for test cases
#    n = int(input()) #input int
#    n,m = map(int,input().split()) #input tuple
#    A = list(map(int,input().split())) #input list
#    s = input() #input string
#    ans = solve(s,L) #solve
#    print(ans) #print single answer
#    print(" ".join(map(str,ans))) #print int array
#
#end of codeforces template

from collections import *

inf = float("inf")

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

n,m = map(int,input().split())
vertices = [i+1 for i in range(n)]
edges = []
for _ in range(m):
    x,y,z = map(int,input().split())
    edges.append((z,x,y))
ans = kruskal(vertices,edges)
if len(ans) == n-1:
    print(sum(x for x,_,_ in ans))
else:
    print("orz")