import itertools

def optimize_assignment(n,cost_func,maximize=False):
    '''
    二分图的最优代价分配：匈牙利算法
    n:元素数量
    cost_func:代价函数，以(i,j)为入参，返回代价值
    maximize:寻找最大(True)/最小(False)代价
    返回值:最优代价，分配方案
    '''
    from scipy.optimize import linear_sum_assignment
    import numpy as np
    cost = np.zeros((n, n))
    for i,j in itertools.product(range(n),range(n)):
        cost[i,j] = cost_func(i,j)
    row,col = linear_sum_assignment(cost,maximize=maximize)
    return int(cost[row,col].sum()),col