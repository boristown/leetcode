# Z 函数（扩展 KMP）
# 对于个长度为n的字符串 。
# 定义函数z[i]表示s和s[i,n-1]（即以s[i]开头的后缀）的最长公共前缀（LCP）的长度。z被称为s的Z函数。
# Python Version
def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = max(0, r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z