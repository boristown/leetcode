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
#define UMII unordered_map<int,int>
#define PUB push_back
#define POB pop_back
#define SORT(L) sort(L.begin(),L.end())
#define RSOR(L) sort(L.rbegin(),L.rend())
#define LOB(A,a) lower_bound(A.begin(),A.end(),a)
#define UPB(A,a) upper_bound(A.begin(),A.end(),a)
#define MALL0(P,T,N) P = (T *)malloc(N * sizeof(T)); memset(P, 0, sizeof(T) * N);
#define MALLI(P,T,N) P = (T *)malloc(N * sizeof(T)); memset(P, 0x3f, sizeof(T) * N);

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
#define UMII unordered_map<int,int>
#define PUB push_back
#define POB pop_back
#define SORT(L) sort(L.begin(),L.end())
#define RSOR(L) sort(L.rbegin(),L.rend())
#define LOB(A,a) lower_bound(A.begin(),A.end(),a)
#define UPB(A,a) upper_bound(A.begin(),A.end(),a)
#define MALL0(P,T,N) P = (T *)malloc(N * sizeof(T)); memset(P, 0, sizeof(T) * N);
#define MALLI(P,T,N) P = (T *)malloc(N * sizeof(T)); memset(P, 0x3f, sizeof(T) * N);

using namespace std;

const int N = 1e5+10;

LL ans[N];
int color[N],vis[N],g_cnt[N];
vector<int> children[N];

map<int,unordered_set<int>> dfs(int idx){
    int ti,el;
    map<int,unordered_set<int>> sorted_counter;
    map<int,int> counter;
    vis[idx] = 1;
    sorted_counter[1].insert(color[idx]);
    counter[color[idx]]=1;
    for(auto j:children[idx]){
        if(vis[j]) continue;
        auto sub_counter = dfs(j);
        for(auto _ti : sub_counter){
            ti = _ti.first;
            for(auto el : _ti.second){
                int c1 = counter[el],c2 = c1+ti;
                if(c1>0) sorted_counter[c1].erase(el);
                sorted_counter[c2].insert(el);
                counter[el]+=ti;
            }
        }
    }
    auto p = sorted_counter.end();
    p--;
    while(!p->second.size()) p--;
    int maxn = p->first;
    for(auto colr : p->second)
        ans[idx] += colr;
    return sorted_counter;
}

LL dfs_fast(int idx){
    vis[idx] = 1;
    LL a = color[idx];
    for(auto j:children[idx]){
        if(vis[j]) continue;
        a+=dfs_fast(j);
    }
    ans[idx] = a;
    return ans[idx];
}

int main() {
    int n,a,b;
    int max_n = 0;
    cin>>n; //input tuple
    REP(i,1,n){
        cin>>color[i];
        g_cnt[color[i]]++;
        max_n = max(max_n,g_cnt[color[i]]);
    }
    REP(i,1,n-1){
        cin>>a>>b;
        children[a].PUB(b);
        children[b].PUB(a);
    }
    if(max_n==1) dfs_fast(1);
    else dfs(1);
    REP(i,1,n){
        cout<<ans[i];
        if(i<n) cout<<" ";
    }
    return 0;
};