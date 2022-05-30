/*
compile g++ main_codeforces.cpp
run .\a

begin of codeforces template (don't delete):

#include <bits/stdc++.h>

#define PUB push_back
#define POB pop_back
#define SORT(L) sort(L.begin(),L.end())

using namespace std;

int main() {
    string s;
    int n,i,j;
    cin >> s; // input string
    cin >> n; // input int
    for(int q=0;q<n;q++){ //loop for input
        cin>>i>>j; //input tuple
    }
    return 0;
};

end of codeforces template 
*/
#include <bits/stdc++.h>

#define PUB push_back
#define POB pop_back
#define SORT(L) sort(L.begin(),L.end())

using namespace std;

class SegTreeLite{

    public:
        int* _sum;
        int _n;

        SegTreeLite(int n){
            _n = n;
            _sum = (int *)malloc(n * 4 * sizeof(int));
            memset(_sum, 0, sizeof(int) * n * 4);
        }

    void _add(int o, int l, int r, int idx, int val) {
        if (l == r) {
            _sum[o] += val;
            return;
        }
        int m = (l + r) / 2;
        if (idx <= m) _add(o * 2, l, m, idx, val);
        else _add(o * 2 + 1, m + 1, r, idx, val);
        _sum[o] = _sum[o * 2] + _sum[o * 2 + 1];
    }

    int _query_sum(int o, int l, int r, int L, int R) {
        if (L <= l && r <= R) return _sum[o];
        int sum = 0;
        int m = (l + r) / 2;
        if (L <= m) sum += _query_sum(o * 2, l, m, L, R);
        if (R > m) sum += _query_sum(o * 2 + 1, m + 1, r, L, R);
        return sum;
    }
    
    int query_sum(int L,int R){
        /*
        Query sum in range [l,r)
        */
        return _query_sum(1,1,_n,L+1,R);
    }
    
    void add(int idx,int val){
        /*
        Increase arr[idx] by val
        */
        _add(1, 1, _n, idx+1, val);
    }
};

int main() {
    string s;
    int n,i,j;
    vector<pair<int,int>> Que;
    vector<pair<int,int>> Ord;
    cin >> s; // input string
    cin >> n; // input int
    for(int q=0;q<n;q++){
        cin>>i>>j;
        Que.PUB({i-1,j});
        Ord.PUB({j,q});
    }
    SORT(Ord);
    int ns = s.size();
    SegTreeLite seg(ns);
    vector<int> st;
    vector<int> ans(n,0);
    int k = -1;
    for(auto& ord : Ord){
        int idx = ord.second;
        int i = Que[idx].first;
        int j = Que[idx].second;
        while(j > k+1){
            k++;
            if(s[k] == '('){
                st.PUB(k);
            }
            else{
                if(st.size()){
                    int k2 = st[st.size()-1];
                    st.POB();
                    seg.add(k2,1);
                }
            }
        }
        ans[idx] = seg.query_sum(i,j);
    }
    for(auto a:ans){
        cout<<(a<<1)<<endl;
    }
    return 0;
};