from itertools import accumulate

class sum_range:
    def __init__(self,arr):
        self.ppsum = list(accumulate(accumulate(arr, initial=0), initial=0))
    
    def get_sum(self,i1,i2,j1,j2):
        '''
        计算长度为n的数组arr中
        所有左端点介于i1,i2之间，右端点介于j1,j2之间的子数组的和
        其中0<=i1<=i2<=j1<=j2<n
        '''
        ans1 = (self.ppsum[i2+1] - self.ppsum[i1]) * (j2+1-j1)
        ans2 = (self.ppsum[j2+2] - self.ppsum[j1+1]) * (i2+1-i1)
        return ans2 - ans1

#以下为sum_range的推导过程
def _sum_range(arr,i1,i2,j1,j2):
    #1. 朴素算法O(n^3)
    ans = 0
    for i in range(i1,i2+1):
        for j in range(j1,j2+1):
            ans += sum(arr[i:j+1])
    #2. 前缀和O(n^2)
    ans = 0
    psum = list(accumulate(arr,initial=0))
    for i in range(i1,i2+1):
        for j in range(j1,j2+1):
            ans += psum[j+1] - psum[i]
    #3. 变形 O(n^2)
    ans = 0
    psum = list(accumulate(arr,initial=0))
    for i in range(i1,i2+1):
        ans -= psum[i]*(j2+1-j1)
        for j in range(j1,j2+1):
            ans += psum[j+1]
    #4. 分离 O(n)
    ans = 0
    psum = list(accumulate(arr,initial=0))
    for i in range(i1,i2+1):
        ans -= psum[i]*(j2+1-j1)
    for j in range(j1,j2+1):
        ans += psum[j+1]*(i2+1-i1)
    #5. 变形 O(n)
    ans1,ans2 = 0,0
    psum = list(accumulate(arr,initial=0))
    for i in range(i1,i2+1):
        ans1 += psum[i]
    ans1 *= j2+1-j1
    for j in range(j1,j2+1):
        ans2 += psum[j+1]
    ans2 *= i2+1-i1
    ans = ans2 - ans1
    #6. 前缀和的前缀和 不考虑ppsum的处理时间（可以提前预处理），时间复杂度为O(1)
    ppsum = list(accumulate(accumulate(arr, initial=0), initial=0))
    ans1 = (ppsum[i2+1] - ppsum[i1]) * (j2+1-j1)
    ans2 = (ppsum[j2+2] - ppsum[j1+1]) * (i2+1-i1)
    ans = ans2 - ans1
    return ans
