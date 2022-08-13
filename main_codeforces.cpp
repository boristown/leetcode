/*
compile & run: 
g++ main_codeforces.cpp
.\a

begin of codeforces template (don't delete):

#include <bits/stdc++.h>

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

using namespace std;

const int N = 1e6+100;

int A[N];

int main() {
    string s;
    int n,a,b;
    int* A;
    cin >> s; // input string
    cin >> n; // input int
    MALL0(A,int,n); // Create Array
    REP(i,1,n){ //loop for input
        cin>>a>>b; //input tuple
        cin>>A[i]; //input array
    }
    return 0;
};

end of codeforces template 
*/
#include <bits/stdc++.h>

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

using namespace std;

//Disjoint Set
class DisjSet
{
  public:
    std::vector<int> parent;
    std::vector<int> size;

  public:
    DisjSet(int max_size) : parent(std::vector<int>(max_size)),
                            size(std::vector<int>(max_size))
    {
        for (int i = 0; i < max_size; ++i){
            parent[i] = i;
            size[i] = 1;
            }
    }
    int find(int x)
    {
        return x == parent[x] ? x : (parent[x] = find(parent[x]));
    }
    void to_union(int x, int y)
    {
        x = find(x);
        y = find(y);
        if(x==y) return;
        int t;
        if (size[x] < size[y])
        {
            t = x;
            x = y;
            y = t;
        }
        parent[y] = x;
        size[x] += size[y];
    }
    bool is_same(int e1, int e2)
    {
        return find(e1) == find(e2);
    }
};

int main() {
    set<tuple<int,int>> CO;
    vector<tuple<int,int>> V;
    V.push_back({0,0});
    int N,M,E,u,v;
    cin>>N>>M>>E;
    REP(i,1,E){
        cin>>u>>v;
        tuple<int,int> tp = {u-1,v-1};
        CO.emplace(tp);
        V.emplace_back(tp);
    }
    int sup = N+M;
    int tot = sup+1;
    auto UF = DisjSet(tot);
    REP(i,N,M+N-1){
        UF.to_union(i,sup);
    }
    int Q,x;
    cin >> Q;
    vector<tuple<int,int>> QL;
    REP(i,1,Q){
        cin>>x;
        QL.emplace_back(V[x]);
        CO.erase(V[x]);
    }
    for(auto x:CO){
        tie(u,v) = x;
        UF.to_union(u,v);
    }
    vector<int> ans;
    REP2(i,Q-1,0){
        tie(u,v) = QL[i];
        int a = UF.size[UF.find(sup)]-M-1;
        ans.emplace_back(a);
        UF.to_union(u,v);
    }
    REP2(i,Q-1,0){
        cout<<ans[i]<<endl;
    }
    /**/
    return 0;
};