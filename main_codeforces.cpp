/*
compile & run: 
g++ main_codeforces.cpp
.\a

begin of codeforces template (don't delete):

#include <bits/stdc++.h>

#define PUB push_back
#define POB pop_back
#define SORT(L) sort(L.begin(),L.end())
#define RSOR(L) sort(L.rbegin(),L.rend())
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
#define RSOR(L) sort(L.rbegin(),L.rend())
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
    n = A.size();
    if(n<2){
        cout<<0<<endl;
        return 0;
    }
    int *V;
    MALL0(V,int,n);
    int i=0;
    for(auto a:A){
        V[i++]=a;
    }
    int ans = 0;
    int pl = 0;
    int pr = n-1;
    int pl2 = 0;
    int pr2 = n-1;
    while(pl2 <= pr2){
        for(int pl=pl2;pl<=pr2;pl++)
        {
            int an = V[pr] % V[pl];
            if(an > ans){
                ans = an;
                while((V[pr] - V[pr2])<=ans) pr2--;
            }
        }
        pr--;
        while((V[pr] - V[pr2])<=ans) pr2--;
        while(V[pl2]<=ans) pl2++;
    }
    cout<<ans<<endl;
    return 0;
};