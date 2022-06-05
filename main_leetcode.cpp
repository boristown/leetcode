/*g++ 

compile & run: 

g++ main_leetcode.cpp
.\a

*/
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int largestPalindrome(int n) {
        if (n == 1) {
            return 9;
        }
        int upper = pow(10, n) - 1;
        for (int left = upper;; --left) { // 枚举回文数的左半部分
            long p = left;
            for (int x = left; x > 0; x /= 10) {
                p = p * 10 + x % 10; // 翻转左半部分到其自身末尾，构造回文数 p
            }
            for (long x = upper; x * x >= p; --x) {
                if (p % x == 0) { // x 是 p 的因子
                    return p % 1337;
                }
            }
        }
    }
};

int main(){
    auto sol = Solution();
    cout<< sol.largestPalindrome(1) << endl;
    return 0;
}
