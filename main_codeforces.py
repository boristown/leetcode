def ok(n,L,S):
    L = L[::-1]
    j = 0
    odd = (n%2==1)
    if not L:
        return True
    while j<n:
        #odd:first must be min
        if odd:
            if L[-1] != S[j]:
                return False
            L.pop()
        #even:first or second must be min
        else:
            if L[-1] != S[j] and L[-2] != S[j]:
                return False
            if L[-1] == S[j]:
                L.pop()
            else:
                a = L.pop()
                b = L.pop()
                L.append(a)
        odd = not odd
        j+=1
    return True

def solve(n,L):
    return "YES" if ok(n,L,sorted(L)) else "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    L = list(map(int,input().split()))
    ans = solve(n,L)
    print(ans)

