#自定义排序器
def mykey(i,a):
    '''
    自定义排序key
    输入：
    i：原顺序
    a：元素值
    返回：
    key：用于排序的tuple
    '''
    return (i,a)

def mysort(L):
    '''
    自定义排序器
    返回排序后的序列
    '''
    Evt = [(mykey(i,a),i,a) for i,a in enumerate(L)]
    Evt.sort()
    return [a for k,i,a in Evt]

def mysort2(L):
    '''
    自定义排序器
    返回排序后的序列（元素，原顺序）
    '''
    Evt = [(mykey(i,a),i,a) for i,a in enumerate(L)]
    Evt.sort()
    return [(a,i) for k,i,a in Evt]