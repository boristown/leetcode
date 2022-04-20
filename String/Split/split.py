#字符串二维分割

def split2(s,c1,c2):
    '''
    s:字符串
    c1:第一维分隔符1
    c2:第二维分隔符2
    返回：二维字符串数组
    '''
    return [a.split(c2) for a in s.split(c1)]