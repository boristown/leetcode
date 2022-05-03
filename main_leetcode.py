import re
from Graph.ShortestPath.Dijkstra import *
from Graph.ShortestPath.SFPA import *
from Graph.ShortestPath.kthPath import *
from Graph.visualize import visualize

if __name__ == "__main__":
    #正权最短路：dijkstra
    adj = {1:[(2,1),(3,3),(5,5)],2:[(4,5)],3:[(4,2),(6,7)],4:[(6,1)],5:[],6:[]}
    print(visualize(adj))
    print("正权最短路：dijkstra:")
    dis = dijkstra(adj,1)
    print(dis)
    #正权第K短路：dijkstra+A*
    print("正权第K短路：dijkstra+A*:")
    dis = dijkstra(adj,1)
    print(dis)
    #负权最短路：SFPA
    adj = {1:[(2,1),(3,-3),(5,5)],2:[(3,-3),(4,5)],3:[(4,-2),(6,-7)],4:[(6,1)],5:[],6:[]}
    print(visualize(adj))
    print("负权最短路：SFPA")
    dis = SPFA(adj,1)
    print(dis)
    #负权最短路：dijkstra(错误结果)
    adj = {1:[(2,1),(3,-3),(5,5)],2:[(3,-3),(4,5)],3:[(4,-2),(6,-7)],4:[(6,1)],5:[],6:[(2,-10)]}
    print(visualize(adj))
    print("负权最短路：dijkstra(错误结果)")
    dis = dijkstra(adj,1)
    print(dis)
    #负环检测：SFPA
    print("负环检测：SFPA")
    dis = SPFA(adj,1)
    print(dis)

