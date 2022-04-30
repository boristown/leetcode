import re
from Graph.ShortestPath.Dijkstra import *
from Graph.ShortestPath.SFPA import *
from Graph.visualize import visualize

if __name__ == "__main__":
    #模式匹配：邮箱
    print("模式匹配：邮箱:")
    s = "boristown@gmail.com"
    pat = "^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
    print("字符串："+s+"\n正则："+pat+"\n匹配结果："+str(re.match(pat,s)))
    #模式匹配：域名
    print("模式匹配：域名:")
    s = "leetcode.cn"
    pat = "[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?"
    print("字符串："+s+"\n正则："+pat+"\n匹配结果："+str(re.match(pat,s)))
    #正权最短路：dijkstra
    print("正权最短路：dijkstra:")
    adj = {1:[(2,1),(3,3),(5,5)],2:[(4,5)],3:[(4,2),(6,7)],4:[(6,1)],5:[],6:[]}
    print(visualize(adj))
    dis = dijkstra(adj,1)
    print(dis)
    #负权最短路：SFPA
    print("负权最短路：SFPA")
    adj = {1:[(2,1),(3,-3),(5,5)],2:[(3,-3),(4,5)],3:[(4,-2),(6,-7)],4:[(6,1)],5:[],6:[]}
    print(visualize(adj))
    dis = SPFA(adj,1)
    print(dis)
    #负权最短路：dijkstra(错误结果)
    print("负权最短路：dijkstra(错误结果)")
    adj = {1:[(2,1),(3,-3),(5,5)],2:[(3,-3),(4,5)],3:[(4,-2),(6,-7)],4:[(6,1)],5:[],6:[(2,-10)]}
    print(visualize(adj))
    dis = dijkstra(adj,1)
    print(dis)
    #负环检测：SFPA
    print("负环检测：SFPA")
    adj = {1:[(2,1),(3,-3),(5,5)],2:[(3,-3),(4,5)],3:[(4,-2),(6,-7)],4:[(6,1)],5:[],6:[(2,-10)]}
    print(visualize(adj))
    dis = SPFA(adj,1)
    print(dis)