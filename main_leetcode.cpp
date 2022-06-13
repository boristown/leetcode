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
#define REP2(i,a,b) for(int i = a; i >= b; i--)
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
    const static int N = 1e5+1;
    int g_ta, g_fu, g_pa, g_n, g_nf;
    LL suf[N],pre[N];

    long long maximumBeauty(vector<int>& fl, long long nf, int ta, int fu, int pa) {
        int n = fl.size();
        SORT(fl);
        LL cost = 0;
        REP2(right,n-1,0){
            if(fl[right]<ta){
                cost += ta-fl[right];
            }
            suf[right] = cost;
        }
        LL pr = 0;
        REP(i,0,n-1){
            pr += fl[i];
            pre[i] = (LL)(i+1)*fl[i] - pr;
        }
        LL ans = 0;
        REP2(right,LOBI(fl,ta),0){
            LL co = suf[right];
            LL le = nf - co;
            if(le<0) break;
            LL an = (LL)(n-right)*fu;
            int left = min((int)(upper_bound(pre,pre+n,le) - pre - 1),right-1);
            if(left>=0) an+=min((LL)(fl[left]+(le-pre[left])/(left+1)),(LL)(ta-1))*pa;
            ans = max(ans,an);
        }
        return ans;
    }
};

int main(){
    auto sol = Solution();
    vector<int> flowers{1,3,1,1};
    cout<< sol.maximumBeauty(flowers,7,6,12,1) << endl;
    vector<int> flowers2{2,4,5,3};
    cout<< sol.maximumBeauty(flowers2,10,5,2,6) << endl;
    return 0;
}
