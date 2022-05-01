def sub_diff(s):
    '''
    统计一个字符串的所有子字符串中的不同字符的总数
    '''
    ans,sum_g,pos = 0,0,[-1]*26
    s = [ord(c) - ord('a') for c in s]
    for i,c in enumerate(s):
        sum_g += i - pos[c]
        ans += sum_g
        pos[c] = i
    return ans