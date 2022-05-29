#计算字符串s中(i,j]的合法括号序列的长度
import bisect

class bracket_range:
    def __init__(self,s):
        self.n = len(s)
        self.s = s
        self.psum = [0]
        self.pbalance = [0]
        self.left = [0]*self.n  #The position of the first ')' to the left of s[i] (with i)
        self.right = [0]*self.n  #The position of the first '(' to the right of s[i] (with i)
        i2,j2 = 0,0
        p,sm=0,0
        j2 = -1
        for i,c in enumerate(s):
            if c==')':
                j2 = i
            self.left[i] = j2
        i2 = self.n
        for i in range(self.n-1,-1,-1):
            if s[i]=='(':
                i2 = i
            self.right[i] = i2
        for c in s:
            if c == '(':
                p+=1
            elif p>0:
                p-=1
                sm+=1
            self.psum.append(sm)
            self.pbalance.append(p)
        
    def get_range(self,i,j):
        '''
        correct bracket length in [i,j)
        '''
        i2,j2 = self.right[i],self.left[j-1]
        if i2 >= j2: return 0
        delta = self.pbalance[i2] - self.pbalance[j2+1]
        ans = self.psum[j2+1] - self.psum[i2]
        if delta > 0:
            ans -= delta
        return ans*2
        
def magic(A,B):
    ans = 0
    return ans

def _bracket(s,i,j):
    #1. 暴力：O(n)
    ans = 0
    b = 0
    for p in range(i,j):
        a = s[p]
        if a == '(':
            b+=1
        elif a == ')':
            if b>0:
                b-=1
            ans+=1
    ans*=2
    #2. 变形：O(n)
    ans,b = 0,0
    for p in range(i,j):
        a = s[p]
        if a == '(':
            b+=1
        else:
            ans = min(ans + 1, b)
    ans*=2
    #3. 再变形: O(n)
    psum = [0]
    p=0
    for c in s:
        if c == '(':
            p+=1
        psum.append(p)
    ans,b = 0,0
    for p in range(i,j):
        a = s[p]
        b = psum[p+1]-psum[i]
        if a == ')':
            ans = min(ans + 1, b)
    ans*=2
    #4. 再变形: O(n)
    ans = psum[i]
    for p in range(i,j):
        if s[p] == ')':
            ans = min(ans + 1, psum[p+1])
    ans = (ans - psum[i])*2
    #5. 再变形: O(n)
    ans = psum[i]
    for p in range(i,j):
        if s[p] == ')' and ans < psum[p+1]:
            ans += 1
    ans = (ans - psum[i])*2
    #6. 魔法： O(1)
    ans = magic(px[i],px[j])
    #7. 假设区间[i,j)中的第一个(出现在i2，最后一个)出现在j2
    #且i2<j2
    #则答案一定在区间[i2,j2+1)内
    return ans