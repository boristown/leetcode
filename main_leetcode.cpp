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
#define SUM_FORE(s,e,E,F,t) int s = 0; for(auto &e : E) {F;s+=t;}
#define MAX_FORI(s,i,a,b,F,t) int s = 0; REP(i,a,b) {F;s=max(s,t);}

class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        
    }
};

int main(){
    auto sol = Solution();
    vector<int> candi{16,17,71,62,12,24,14};
    cout<< sol.largestCombination(candi) << endl;
    return 0;
}
