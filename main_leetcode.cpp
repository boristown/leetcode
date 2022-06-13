/*g++ 

compile & run: 

g++ main_leetcode.cpp
.\a

*/
#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
#define VI vector<int>
#define VLL vector<LL> VLL
#define REP(i,a,b) for(int i = a; i <= b; i++)
#define UMII unordered_map<int,int>
#define PUB push_back
#define POB pop_back
#define SORT(L) sort(L.begin(),L.end());
#define RSOR(L) sort(L.rbegin(),L.rend());
#define LOB(A,a) lower_bound(A.begin(),A.end(),a)
#define UPB(A,a) upper_bound(A.begin(),A.end(),a)
#define LOBI(A,a) lower_bound(A.begin(),A.end(),a)-A.begin()
#define UPBI(A,a) upper_bound(A.begin(),A.end(),a)-A.begin()
#define MALL0(P,T,N) P = (T *)malloc(N * sizeof(T)); memset(P, 0, sizeof(T) * N);
#define MALLI(P,T,N) P = (T *)malloc(N * sizeof(T)); memset(P, 0x3f, sizeof(T) * N);
#define LEN(i,A) int i = A.size();

class Solution {
public:
    int g_ta, g_fu, g_pa, g_n;
    LL get_val(vector<int>& fl, int left, int right){
        //n - right * 
    }

    long long maximumBeauty(vector<int>& fl, long long nf, int ta, int fu, int pa) {
        int n = fl.size();
        SORT(fl);
        g_n = n;
        g_ta = ta;
        g_fu = fu;
        g_pa = pa;
        int right = LOBI(fl,ta);
        int left = 0;
        int ans = 0;
        int val = ;
        return 0;
    }
};

int main(){
    auto sol = Solution();
    vector<int> flowers{1,3,1,1};
    cout<< sol.maximumBeauty(flowers,7,6,12,1) << endl;
    return 0;
}
