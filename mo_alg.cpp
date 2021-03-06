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

const int N = 1e6+100;

int L, R;
int A[N],pos[N];
LL ans[N],Ans,cnt[N];

struct Node{
    int l,r,id;
    bool operator < (Node xx) const{
        if(pos[l] == pos[xx.l]) return r < xx.r;
        else return pos[l] < pos[xx.l];
    }
}Q[N];

void add(int x){
    Ans += A[x] * (2 * cnt[A[x]] + 1);
    cnt[A[x]]++;

}

void del(int x){
    cnt[A[x]]--;
    Ans -= A[x] * (2 * cnt[A[x]] + 1);
}

int main() {
    int n,t,a;
    cin>>n>>t; //input tuple
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

        ans[Q[i].id] = Ans;
    }
    REP(i,1,t){
        cout<<ans[i]<<endl;
    }
    return 0;
};