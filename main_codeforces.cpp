/*
compile & run: 
g++ main_codeforces.cpp
.\a

begin of codeforces template (don't delete):

#include <bits/stdc++.h>

#define VI vector<int>
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

int main() {
    string s;
    int n,a,b;
    int* A;
    cin >> s; // input string
    cin >> n; // input int
    MALL0(A,int,n); // Create Array
    for(int i=0;i<n;i++){ //loop for input
        cin>>a>>b; //input tuple
        cin>>A[i]; //input array
    }
    return 0;
};

end of codeforces template 
*/
#include <bits/stdc++.h>

#define VI vector<int>
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

int main() {
    int n,t,a;
    cin>>n>>t; //input tuple
    VI A;
    for(int i=0;i<n;i++){ //loop for input
        cin>>a; //input tuple
        A.PUB(a);
    }
    int l,r;
    for(int i=0;i<t;i++){
        cin>>l>>r;
        l--;
        r--;
        UMII cnt;
        for(int j=l;j<=r;j++){
            if(!cnt.count(A[j])){
                cnt[A[j]]=0;
            }
            cnt[A[j]]++;
        }
        long long ans = 0;
        for(auto k :cnt){
            ans+=(long long)(k.first)*k.second*k.second;
        }
        cout<<ans<<endl;
    }
    return 0;
};