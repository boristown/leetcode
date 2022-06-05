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
    vector<vector<pair<int,int>>> A;
    UMII cnt;
    UMII cnt2;
    for(int i=0;i<n;i++){ //loop for input
        cin>>a; //input tuple
        cnt[a]++;
        int c = cnt[a];
        cnt2[c]+=a;
        if(c>A.size()) A.PUB(vector<pair<int,int>>());
        A[c-1].PUB({i,cnt2[c]});
    }
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