class Manacher:
    '''
    马拉车算法O(n)
    计算字符串的所有回文信息
    https://oi-wiki.org/string/manacher/
    '''
    def __init__(self,s):
        self.s = s
        self.n = len(s)
    
    def get_odd(self):
        '''
        获取每个中心点的奇回文半径
        '''
        # Python Version
        d1 = [0] * self.n
        l, r = 0, -1
        for i in range(0, self.n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while 0 <= i - k and i + k < self.n and self.s[i - k] == self.s[i + k]:
                k += 1
            d1[i] = k
            k -= 1
            if i + k > r:
                l = i - k
                r = i + k
        return d1

    def get_even(self):
        '''
        获取每个中心点的偶回文半径
        '''
        # Python Version
        d2 = [0] * self.n
        l, r = 0, -1
        for i in range(0, self.n):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
            while 0 <= i - k - 1 and i + k < self.n and self.s[i - k - 1] == self.s[i + k]:
                k += 1
            d2[i] = k
            k -= 1
            if i + k > r:
                l = i - k - 1
                r = i + k
        return d2