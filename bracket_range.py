#计算字符串s中(i,j]的合法括号序列的长度

class bracket_range:
    def __init__(self,s):
        p1,p2,self.psum1,self.psum2 = 0,0,[0],[0]
        for a in s:
            if a == '(':
                p1+=1
            else:
                p2+=1
            self.psum1.append(p1)
            self.psum2.append(p2)
        
    def get_range(self,i,j):
        '''
        correct bracket length in [i,j)
        '''
        s1 = self.psum1[j]-self.psum1[i]
        s2 = self.psum2[j]-self.psum2[i]
        ans = min(s1,s2)
        return ans*2

def _bracket(s,i,j):
    #暴力：O(n)
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
    #前缀和：O(1)
    ans = 0
    p1,p2,psum1,psum2 = 0,0,[0],[0]
    for a in s:
        if a == '(':
            p1+=1
        else:
            p2+=1
        psum1.append(p1)
        psum2.append(p2)
    s1 = psum1[j]-psum1[i]
    s2 = psum2[j]-psum2[i]
    ans = min(s1,s2)
    return ans