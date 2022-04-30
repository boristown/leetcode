import re
from Graph.ShortestPath.Dijkstra import dijkstra
from Graph.visualize import visualize

if __name__ == "__main__":
    print("re:")
    pat = "^(.+?\D)?0\d"
    print(not re.match(pat,"1+051"))
    print(not re.match(pat,"05+1"))

if __name__ == '__main__':
    print("dijkstra:")
    e = {1:[(2,1),(3,3)],2:[(4,5)],3:[(4,2)],4:[]}
    print(visualize(e))
    dis = dijkstra(e,1)
    print(dis)