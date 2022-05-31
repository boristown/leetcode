/*
compile: 
g++ main_codeforces.cpp
run:
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
    int n;
    int* A;
    cin >> n; // input int
    MALL0(A,int,n);
    for(int i=0;i<n;i++){ //loop for input
        cin>>A[i]; //input tuple
    }
    int ans = 0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++){
            if(A[i]>A[j]){
                ans = max(ans,A[i]%A[j]);
            }
        }
    }
    cout<<ans<<endl;
    return 0;
};