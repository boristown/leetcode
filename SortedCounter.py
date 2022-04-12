from sortedcontainers import *
from collections import *

class SortedCounter:
    '''
    适用范围：有序计数器
    '''
    def __init__(self):
        self.C = Counter()
        self.S = SortedList()
        
    def inc(self, key: str) -> None:
        self.C[key]+=1
        n=self.C[key]
        if n>=1:
            self.S.discard((n-1,key))
        self.S.add((n,key))
        
    def dec(self, key: str) -> None:
        self.C[key]-=1
        n=self.C[key]
        self.S.discard((n+1,key))
        if n:
            self.S.add((n,key))

    def getMaxKey(self) -> str:
        return self.S[-1][1] if self.S else ""

    def getMinKey(self) -> str:
        return self.S[0][1] if self.S else ""

    def most_common(self,n=0) -> list:
        if n:
            return list(self.S[:n])
        else:
            return list(self.S)



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()