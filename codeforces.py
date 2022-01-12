INF = float("inf")
n,l,k = map(int,input().split())
L = list(map(int,input().split()))
M = list(map(int,input().split()))
L.append(l)
while k>0:
    maxloss = 0
    maxI = 0
    for i in range(1,n):
        if M[i] > M[i-1]:
            loss = (L[i+1] - L[i]) * (M[i] - M[i-1])
            if loss > maxloss:
                maxloss = loss
                maxI = i
    if maxI:
        del M[maxI]
        del L[maxI]
        n-=1
        k-=1
    else:
        break
ans = 0
for i in range(1,n+1):
    ans += (L[i] - L[i-1])*M[i-1]
print(ans)