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
#define SUM_E(s,E) long s = 0; for(auto &e : E) {s+=e;}
#define MAX_E(s,E) long s = 0; for(auto &e : E) {s=max(s,e);}
#define MIN_E(s,E) long s = LONG_MAX; for(auto &e : E) {s=min(s,e);}
#define SUM_FORE(s,e,E,F,t) long s = 0; for(auto &e : E) {F;s+=t;}
#define SUM_FORI(s,i,a,b,F,t) long s = 0; REP(i,a,b) {F;s+=t;}
#define MAX_FORE(s,e,E,F,t) long s = 0; for(auto &e : E) {F;s=max(s,t);}
#define MAX_FORI(s,i,a,b,F,t) long s = 0; REP(i,a,b) {F;s=max(s,t);}
#define MIN_FORE(s,e,E,F,t) long s = LONG_MAX; for(auto &e : E) {F;s=min(s,t);}
#define MIN_FORI(s,i,a,b,F,t) long s = LONG_MAX; REP(i,a,b) {F;s=min(s,t);}
#define UMP unordered_map
#define UST unordered_set
#define UNION(A,B,C) C=A; for(auto &b:B) C.insert(b);
#define INTERSECTION(A,B,C) C.clear(); for(auto &b:B) if(A.count(b)) C.insert(b);
#define DIFFERENCE(A,B,C) C=A; for(auto &b:B) if(C.count(b)) C.erase(b);

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
#define SUM_E(s,E) long s = 0; for(auto &e : E) {s+=e;}
#define MAX_E(s,E) long s = 0; for(auto &e : E) {s=max(s,e);}
#define MIN_E(s,E) long s = LONG_MAX; for(auto &e : E) {s=min(s,e);}
#define SUM_FORE(s,e,E,F,t) long s = 0; for(auto &e : E) {F;s+=t;}
#define SUM_FORI(s,i,a,b,F,t) long s = 0; REP(i,a,b) {F;s+=t;}
#define MAX_FORE(s,e,E,F,t) long s = 0; for(auto &e : E) {F;s=max(s,t);}
#define MAX_FORI(s,i,a,b,F,t) long s = 0; REP(i,a,b) {F;s=max(s,t);}
#define MIN_FORE(s,e,E,F,t) long s = LONG_MAX; for(auto &e : E) {F;s=min(s,t);}
#define MIN_FORI(s,i,a,b,F,t) long s = LONG_MAX; REP(i,a,b) {F;s=min(s,t);}
#define UMP unordered_map
#define UST unordered_set
#define UNION(A,B,C) C=A; for(auto &b:B) C.insert(b);
#define INTERSECTION(A,B,C) C.clear(); for(auto &b:B) if(A.count(b)) C.insert(b);
#define DIFFERENCE(A,B,C) C=A; for(auto &b:B) if(C.count(b)) C.erase(b);

using namespace std;

const static int N = 2e5+100;

LL A[N];

string zfill(string s,int n){
    ostringstream oss;
    oss.setf(ios::right);
    oss.fill('0');
    oss.width(n);
    oss << s;
    return oss.str();
}

int main() {
    int t,n;
    string s;
    cin>>t;
    REP(i,1,t){
        cin>>s>>n;
        cout<<zfill(s,n)<<endl;
    }
    return 0;
};