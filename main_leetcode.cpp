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
#define SUM_E(s,E) long s = 0; for(auto &e : E) {s+=e;}
#define MAX_E(s,E) long s = 0; for(auto &e : E) {s=max(s,e);}
#define MIN_E(s,E) long s = LONG_MAX; for(auto &e : E) {s=min(s,e);}
#define SUM_FORE(s,e,E,F,t) long s = 0; for(auto &e : E) {F;s+=t;}
#define SUM_FORI(s,i,a,b,F,t) long s = 0; REP(i,a,b) {F;s+=t;}
#define MAX_FORE(s,e,E,F,t) long s = 0; for(auto &e : E) {F;s=max(s,t);}
#define MAX_FORI(s,i,a,b,F,t) long s = 0; REP(i,a,b) {F;s=max(s,t);}
#define MIN_FORE(s,e,E,F,t) long s = LONG_MAX; for(auto &e : E) {F;s=min(s,t);}
#define MIN_FORI(s,i,a,b,F,t) long s = LONG_MAX; REP(i,a,b) {F;s=min(s,t);}
#define UMP unordered_map
#define UST unordered_set
#define UNION(A,B,C) C=A; for(auto &b:B) C.insert(b);
#define INTERSECTION(A,B,C) C.clear(); for(auto &b:B) if(A.count(b)) C.insert(b);
#define DIFFERENCE(A,B,C) C=A; for(auto &b:B) if(C.count(b)) C.erase(b);

class Solution {
public:
    long long distinctNames(vector<string>& ideas) {
        LEN(n,ideas);
        LL ans = 0;
        UMP<char,UST<string>> suf_set;
        UST<char> pre_all;
        for(auto &e : ideas){
            LEN(len,e);
            auto pre = e[0];
            auto suf = e.substr(1,len-1);
            suf_set[pre].insert(suf);
            pre_all.insert(pre);
        }
        for(char a = 'a';a<'z';a++){
            for(char b=a+1;b<='z';b++)
            {
                UST<string> stc;
                INTERSECTION(suf_set[a],suf_set[b],stc);
                LL k = stc.size();
                ans+=2*(suf_set[a].size()-k)*(suf_set[b].size()-k);
            }
        }
        return ans;
    }
};

int main(){
    auto sol = Solution();
    vector<string> ideas{"coffee","donuts","time","toffee"};
    cout<< sol.distinctNames(ideas) << endl;
    vector<string> ideas2{"aaa","baa","caa","bbb","cbb","dbb"};
    cout<< sol.distinctNames(ideas2) << endl;
    return 0;
}
