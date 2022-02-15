def matrix(m,n,val=0):
    '''
    定义一个m行n列的值为val的矩阵
    '''
    return [[val] * n for _ in range(m)]

def matrix_dim(M):
    '''
    获取矩阵M的行列数
    '''
    return len(M),len(M[0])

def matrix_transpose(M):
    '''
    返回矩阵M的行列转置矩阵
    '''
    m,n = matrix_dim(M)
    T = matrix(n,m)
    for i in range(m):
        for j in range(n):
            T[j][i] = M[i][j]
    return T

def matrix_col(M,j):
    '''
    获取矩阵M的第j列
    '''
    return [M[i][j] for i in range(len(M))]

def matrix_row_max(M,index=False):
    '''
    获取矩阵每一行的最大值/坐标(降维)
    M:矩阵
    index:是否同时获取坐标
    '''
    row_max = [max(M[i]) for i in range(M)]
    if not index:
        return row_max
    col_ind = [M[i].index(row_max[i]) for i in range(M)]
    return row_max,col_ind

def matrix_row_min(M,index=False):
    '''
    获取矩阵每一行的最小值/坐标(降维)
    M:矩阵
    index:是否同时获取坐标
    '''
    row_min = [min(M[i]) for i in range(M)]
    if not index:
        return row_min
    col_ind = [M[i].index(row_min[i]) for i in range(M)]
    return row_min,col_ind

def matrix_col_max(M,index=False):
    '''
    获取矩阵每一列的最大值/坐标(降维)
    M:矩阵
    index:是否同时获取坐标
    '''
    return matrix_row_max(matrix_transpose(M))

def matrix_col_min(M,index=False):
    '''
    获取矩阵每一列的最小值/坐标(降维)
    M:矩阵
    index:是否同时获取坐标
    '''
    return matrix_row_min(matrix_transpose(M))

def matrix_max(M,index=False):
    '''
    获取矩阵的最大值/坐标
    M:矩阵
    index:是否同时获取坐标
    '''
    if index:
        row_max,row_ind = matrix_row_max(M,True)
        row_max_max = max(row_max)
        row_max_ind = row_max.index(row_max_max)
        return row_max_max,(row_max_ind,row_ind[row_max_ind])
    else:
        return max(matrix_row_max(M))