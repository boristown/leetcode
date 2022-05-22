from functools import cache

def alpha_beta(state,move,score):
    '''
    博弈(Alpha-Beta剪枝)
    https://github.com/boristown/leetcode/blob/main/alpha_beta.py
    假设Alice、Bob都采用最优策略，Alice先手，返回Alice的最终得分
    state:初始状态
    move(state):下一个状态
    score(state):结点分数(‘#’表示该节点不是最终节点，无法计算得分)
    '''
    inf = float("inf")
    @cache
    def dp(state,alpha,beta,is_max):
        v = score(state)
        if v != '#': return v
        next_is_max = not is_max
        for next_state in move(state):
            sco = dp(next_state,alpha,beta,next_is_max)
            if is_max: #MAX结点，扩大下界
                alpha = max(alpha,sco)
            else: #MIN结点，缩小上界
                beta = min(beta,sco)
            if alpha>=beta: #alpha-beta剪枝
                break
        return alpha if is_max else beta
    return dp(state,-inf,inf,True)