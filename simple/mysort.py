#自定义排序器
#返回排序后的序列（元素，原顺序）
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
    Evt = [(mykey(i,a),i,a) for i,a in enumerate(L)]
    Evt.sort()
    return [(a,i) for k,i,a in Evt]