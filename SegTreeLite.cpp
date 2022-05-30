#include <bits/stdc++.h>

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