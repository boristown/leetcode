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

using namespace std;

const static int N = 2e5+100;

LL A[N];

int main() {
    int t,n;
    cin>>t;
    REP(i,1,t){
        cin>>n;
        unordered_map<LL,vector<int>> MV;
        unordered_map<LL,vector<int>> pre;
        vector<int> IDX;
        LL temp;
        A[0]=0;
        REP(j,1,n){
            cin>>temp;
            MV[temp].PUB(j);
        }
        int an,anss=0;
        int left = 1,right = 1,ans = 0;
        for(auto &IT:MV){
            tie(temp,IDX) = IT;
            pre[temp].PUB(0);
            int cum = 0;
            int last = -1;
            int mn = 0;
            int mni = IDX[0]-1;
            for(auto idx:IDX){
                if(last==-1){
                    cum++;
                }
                else{
                    cum += 1 - (idx-last-1);
                }
                an = cum-mn;
                if(an>anss){ 
                    anss = an;
                    ans = temp;
                    left = mni+1;
                    right = idx;
                }
                pre[temp].PUB(cum);
                if(cum<mn) {mn = cum;mni = idx;}
                last = idx;
            }
        }
        cout<<ans<<" "<<left<<" "<<right<<endl;
    }
    return 0;
};