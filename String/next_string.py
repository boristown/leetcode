#Get the lexicographically next string

def next_string(s):
    ans = list(s)
    i = len(s) - 1
    while i>=0:
        a = s[i]
        if a == 'z':
            b = 'a'
            ans[i] = b
            i-=1
        else:
            b = chr(ord(a)+1)
            ans[i] = b
            break
    else:
        ans.append('a')
    ans2 = "".join(ans)
    return ans2