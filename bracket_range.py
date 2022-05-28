#计算字符串s中(i,j]的合法括号序列的长度

class bracket_range:
    def __init__(self,s):
        self.s = s
        self.psum = [0]
        p=0
        for c in s:
            if c == '(':
                p+=1
            self.psum.append(p)
        
    def get_range(self,i,j):
        '''
        correct bracket length in [i,j)
        '''
        ans = self.psum[i]
        for p in range(i,j):
            if self.s[p] == ')' and ans < self.psum[p+1]:
                ans += 1
        ans = (ans - self.psum[i])*2
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
    return ans