/*
compile & run: 
g++ main_codeforces.cpp
.\a

begin of codeforces template (don't delete):

#include <bits/stdc++.h>

#define PUB push_back
#define POB pop_back
#define SORT(L) sort(L.begin(),L.end())
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

#define PUB push_back
#define POB pop_back
#define SORT(L) sort(L.begin(),L.end())
#define MALL0(P,T,N) P = (T *)malloc(N * sizeof(T)); memset(P, 0, sizeof(T) * N);
#define MALLI(P,T,N) P = (T *)malloc(N * sizeof(T)); memset(P, 0x3f, sizeof(T) * N);

using namespace std;

int main() {
    int n,a;
    set<int> A;
    cin >> n; // input int
    for(int i=0;i<n;i++){ //loop for input
        cin>>a; //input tuple
        if(a>1)
            A.insert(a);
    }
    if(!A.size()){
        cout<<0<<endl;
        return 0;
    }
    int ans = 0;
    auto pmax = A.end();
    for(int i = 0;i<100;i++){
        pmax--;
        if(pmax == A.begin()){
            break;
        }
        for(auto pbase = pmax;*pbase > ans;){
            pbase--;
            ans = max(ans,(*pmax) % (*pbase));
            if(pbase==A.begin())
                break;
        }
    }
    cout<<ans<<endl;
    return 0;
};