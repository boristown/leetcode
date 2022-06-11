/*
compile & run: 
g++ main_codeforces.cpp
.\a

begin of codeforces template (don't delete):

#include <bits/stdc++.h>

typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VLL;
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
typedef vector<int> VI;
typedef vector<LL> VLL;
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

int L, R;
int A[N],pos[N];
LL ans[N],Ans,flag[N];


struct Node{
    int l,r,id;
    bool operator < (Node xx) const{
        if(pos[l] == pos[xx.l]) return r < xx.r;
        else return pos[l] < pos[xx.l];
    }
}Q[N];

void add(int x){
}

void del(int x){
}

int main() {
    int n,t,a;
    cin>>n>>t; //input tuple
    UMII cnt;
    UMII cnt2;
    int sz = sqrt(n);
    REP(i,1,n){
        cin>>A[i];
        pos[i] = i/sz;
    }
    REP(i,1,t){
        cin>>Q[i].l>>Q[i].r;
        Q[i].id = i;
    }
    sort(Q+1,Q+1+t);
    REP(i,1,t){
        while(L < Q[i].l) del(L),L++;

        while(L > Q[i].l) L--, add(L);

        while(R < Q[i].r) R++, add(R);

        while(R > Q[i].r) del(R), R--;

        ans[Q[i].id] = 0;
    }
    for(int i=0;i<n;i++){ //loop for input
        cin>>a; //input tuple
        cnt[a]++;
        int c = cnt[a];
        cnt2[c]+=a;
        if(c>A.size()) A.PUB(vector<pair<int,int>>());
        A[c-1].PUB({i,cnt2[c]});
    }
    L = 1, R = 0;
    int l,r;
    for(int i=0;i<t;i++){
        cin>>l>>r;
        r--;
        l--;
        long long ans = 0;
        for(int c=0;c<A.size();c++){
            
        }
        for(auto& k:A){
            int len = UPB(k.second,r) - LOB(k.second,l);
            if(len) ans+=(long long)(k.first)*len*len;
        }
        cout<<ans<<endl;
    }
    return 0;
};