from sortedcontainers import *
from collections import *

class SortedCounter:
    '''
    适用范围：有序计数器
    '''
    def __init__(self):
        self.C = Counter()
        self.S = SortedList(lambda x:-x)
        
    def inc(self, key: str, m: int) -> None:
        tmp = self.C[key]
        self.C[key]+=m
        n=self.C[key]
        if tmp>0:
            self.S.discard((tmp,key))
        self.S.add((n,key))
        
    def dec(self, key: str, m: int) -> None:
        tmp = self.C[key]
        if tmp == 0:
            return
        self.C[key]-=m
        n=self.C[key]
        self.S.discard((tmp,key))
        if n:
            self.S.add((n,key))

    def getMaxKey(self) -> str:
        return self.S[0][1] if self.S else ""

    def getMinKey(self) -> str:
        return self.S[-1][1] if self.S else ""

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