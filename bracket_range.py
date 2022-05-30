#计算字符串s中(i,j]的合法括号序列的长度
class bracket_range:
    def __init__(self,s,Q):
        self.sl = SortedList()
        st = []
        n = len(s)
        matched = 0
        #self.psum = []
        Evt = [(q[1],q[0],i) for i,q in enumerate(Q)]
        n_ans = len(Q)
        self.ans = [0]*n_ans
        Evt.sort()
        k = -1
        for j,i,idx in Evt:
            while j > k+1:
                k+=1
                a = s[k]
                if a == '(':
                    st.append(k)
                else:
                    if st:
                        k2 = st.pop()
                        self.sl.add((k2,k))
                        matched+=1
                #self.psum.append(matched)
            self.ans[idx] = (matched - self.sl.bisect_left((i,0))) * 2
        
    def get_range(self,i,j):
        '''
        correct bracket length in [i,j)
        '''
        a = self.psum[j-1]
        b = self.sl.bisect_left((i,0))
        return (a-b)*2
        
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