import heapq
#优先队列
class PQ:
    def __init__(self,Q,big):
        self.Q = Q
        self.big = big
        if big:
            for i in range(len(Q)):
                Q[i] *= -1
        heapq.heapify(self.Q)

    def push(self,it):
        if self.big:
            heapq.heappush(self.Q,-it)
        else:
            heapq.heappush(self.Q,it)
    
    def pop(self):
        it = heapq.heappop(self.Q)
        if self.big:
            return -it
        else:
            return it