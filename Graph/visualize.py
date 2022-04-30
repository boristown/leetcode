# 将邻接表存储的图可视化为可视化的ascii图像
# by BorisTown/ak-bot
# 2022-4-30

def visualize_edge(u,v,w):
    ans = ""
    ans = str(u) + "->" + str(v) + "(" + str(w) + ")"
    return ans

def visualize(graph):
    ans = ["Graph:"]
    for u in graph:
        for v,w in graph[u]:
            ans.append(visualize_edge(u,v,w))
    return "\n".join(ans)