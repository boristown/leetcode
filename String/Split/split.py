#字符串二维分割

def split2(s,c1,c2):
    '''
    s:字符串
    c1:第一维分隔符1
    c2:第二维分隔符2
    返回：二维数组
    '''
    ans = []
    for a in s.split(c1):
        ans.append(a.split(c2))
    return ans