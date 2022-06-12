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

const LL N = 1e5+10;

LL ans[N];
LL color[N],vis[N],dis[N],parent[N],pos[N],max_dis;
vector<LL> children[N];

void op(LL idx,LL val){
    if(val>=dis[idx]) return;
    dis[idx] = val;
    max_dis = max(max_dis,val);
    //op(parent[idx],val+1);
    for(auto j:children[idx]){
        op(j,val+1);
    }
}

int main() {
    LL n,m,a,b;
    LL max_child = 0;
    set<LL> sorted_st;
    cin>>n>>m; //input tuple
    memset(dis, 0x3f, sizeof(LL) * N);
    REP(i,1,n-1){
        cin>>a>>b;
        children[a].PUB(b);
        children[b].PUB(a);
        //max_child = max(max_child,(LL)children[a].size());
        //max_child = max(max_child,(LL)children[b].size());
        //parent[b] = a;
    }
    op(1,0);
    if(max_dis<n-1)
    {
        REP(i,1,m){
            LL ti,vi;
            cin>>ti>>vi;
            if(ti==1){
                op(vi,0);
            }
            else{
                cout<<dis[vi]<<endl;
            }
        }
    }
    else{
        sorted_st.insert(dis[1]);
        REP(i,1,m){
            int ti,vi;
            cin>>ti>>vi;
            if(ti==1){
                sorted_st.insert(dis[vi]);
            }
            else{
                auto pos = sorted_st.upper_bound(dis[vi]);
                LL min_dis = N+1;
                if(pos!=sorted_st.end()) min_dis = min(min_dis,abs((*pos)-dis[vi]));
                pos--;
                min_dis = min(min_dis,abs(dis[vi]-(*pos)));
                cout<<min_dis<<endl;
            }
        }
    }
    return 0;
};