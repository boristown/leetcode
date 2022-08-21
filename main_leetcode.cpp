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
#define VEC_FORE(T,vt,e,E,cond,F,t) vector<T> vt; for(auto &e : E) if(cond) {F;vt.emplace_back(t);}
#define VEC_FORI(T,vt,i,a,b,cond,F,t) vector<T> vt; REP(i,a,b) if(cond) {F;vt.emplace_back(t);}
#define UMP unordered_map
#define UST unordered_set
#define UNION(A,B,C) C=A; for(auto &b:B) C.emplace(b);
#define INTERSECTION(A,B,C) C.clear(); for(auto &b:B) if(A.count(b)) C.emplace(b);
#define DIFFERENCE(A,B,C) C=A; for(auto &b:B) if(C.count(b)) C.erase(b);

class Solution {
public:
    long long kSum(vector<int>& nums, int k) {
        SORT(nums);
        int p = LOBI(nums,0);
        VI posi;
        VI nega;
        LL mx;
        SUM_E(mx,posi);
        if(k == 1) return mx;
        priority_queue<int> hq;
        hq.push(-mx);
        int cnt = 0;
        for(int i=nega.size()-1;i>=0;i--){
            int a = nega[i];
            priority_queue<int> hq2 = hq;
            for(int i = 0; i < hq2.size(); i++){ // 这里只会遍历一次
                int b = hq2.top();
                hq2.pop();
                int c = a+b;
                hq.push(-c);
                if(hq.size()>k){
                    hq.pop();
                }
            }
            cnt ++;
            if(cnt==k){
                break;
            }
        }
        cnt = 0;
        for(int i=0;i<posi.size();i++){
            int a = -posi[i];
            priority_queue<int> hq2 = hq;
            for(int i = 0; i < hq2.size(); i++){ // 这里只会遍历一次
                int b = hq2.top();
                hq2.pop();
                int c = a+b;
                hq.push(-c);
                if(hq.size()>k){
                    hq.pop();
                }
            }
            cnt ++;
            if(cnt==k){
                break;
            }
        }
        return -hq.top();
    }
};


int main(){
    int t=0;
    string str;
    getline(cin,str);
    t = stoi(str);
    VI vi;
    REP(i,1,t){
        auto sol = Solution();
        getline(cin,str);
        int k = stoi(str);
        cout<< sol.kSum(vi,k) << endl;
    }
    return 0;
}
