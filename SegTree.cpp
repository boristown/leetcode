#include <bits/stdc++.h>

using namespace std;

class SegTree{
    /*
    通用线段树 by AK自动机
    支持增量更新，覆盖更新，序列更新，任意RMQ操作
    基于二叉树实现
    初始化：O(1)
    增量更新或覆盖更新的单次操作复杂度：O(log k)
    序列更新的单次复杂度：O(n)
    https://github.com/boristown/leetcode/blob/main/SegTree.cpp
    */
   public:
        long _default,_ans;
        long (*_f1)(long,long),(*_f2)(long,long);
        long _l,_r,_v,_lazy_tag;
        SegTree *_left, *_right;

    SegTree(long (*f1)(long,long),long (*f2)(long,long), long l, long r, long v = 0){
        /*
        初始化线段树[left,right)
        f1,f2示例：
        线段和:
        long f1(long a,long b){
            return a+b;
        }
        long f2(long a,long n){
            return a*n;
        }
        线段最大值:
        long f1(long a,long b){
            return max(a,b);
        }
        long f2(long a,long n){
            return a;
        }
        线段最小值:
        long f1(long a,long b){
            return min(a,b);
        }
        long f2(long a,long n){
            return a;
        }
        */
        _default = v;
        _ans = (*f2)(v,r-l);
        _f1 = f1;
        _f2 = f2;
        _l = l; //left
        _r = r; //right
        _v = v; //init value
        _lazy_tag = 0; //Lazy tag
        _left = nullptr; //SubTree(left,bottom)
        _right = nullptr; //SubTree(right,bottom)
    }

    long get_mid(){
        return (_l + _r) / 2;
    }

    void create_subtrees(){
        long mid = get_mid();
        if(_left == nullptr && mid > _l)
            _left = new SegTree(_f1, _f2, _l, mid, _default);
        if(_right == nullptr)
            _right = new SegTree(_f1, _f2, mid, _r, _default);
    }

    long build(vector<long> arr){
        /*
        将线段树的值初始化为arr
        输入保证arr与线段大小一致
        */
        long m0 = arr[0];
        long len = arr.size();
        _lazy_tag = 0;
        if(_r == _l+1){
            _v = m0;
            _ans = (*_f2)(m0,arr.size());
            return _ans;
        }
        _v = -1;
        long mid = get_mid();
        create_subtrees();
        vector<long> arr_l;
        vector<long> arr_r;
        for(int i=0;i<len;i++){
            if(i<mid-_l)
                arr_l.emplace_back(arr[i]);
            else
                arr_r.emplace_back(arr[i]);
        }
        _ans = _f1(_left->build(arr_l), _right->build(arr_r));
        return _ans;
    }

    long cover_seg(long l,long r,long v){
        /*
        将线段[left,right)覆盖为val
        */
        if(_v == v || l >= _r || r <= _l) return _ans;
        if(l <= _l && r >= _r){
            _v = v;
            _lazy_tag = 0;
            _ans = _f2(v,_r-_l);
            return _ans;
        }
        create_subtrees();
        if(_v != -1){
            if(_left){
                _left->_v = _v;
                _left->_ans = _f2(_v,_left->_r - _left->_l);
                }
            if(_right){
                _right->_v = _v;
                _right->_ans = _f2(_v,_right->_r - _right->_l);
            }
            _v = -1;
        }
        //push up
        _ans = _f1(_left->cover_seg(l, r, v), _right->cover_seg(l, r, v));
        return _ans;
    }

    long inc_seg(long l,long r,long v){
        /*
        将线段[left,right)增加val
        */
        if(v == 0 || l >= _r || r <= _l) return _ans;
        //_ans = '?'
        if(l <= _l && r >= _r){
            if(_v == -1)
                _lazy_tag += v;
            else
                _v += v;
            _ans += _f2(v,_r-_l);
            return _ans;
        }
        create_subtrees();
        if(_v != -1){
            _left->_v = _v;
            _left->_ans = _f2(_v,_left->_r-_left->_l);
            _right->_v = _v;
            _right->_ans = _f2(_v,_right->_r-_right->_l);
            _v = -1;
        }
        pushdown();
        _ans = _f1(_left->inc_seg(l, r, v),_right->inc_seg(l, r, v));
        return _ans;
    }

    long inc_idx(long idx,long v){
        /*
        increase idx by val
        */
        if(v == 0 || idx >= _r || idx < _l)
            return _ans;
        if(idx == _l && _l == _r - 1){
            _v += v;
            _ans += _f2(v,1);
            return _ans;
        }
        create_subtrees();
        if(_v != -1){
            _left->_v = _v;
            _left->_ans = _f2(_v,_left->_r-_left->_l);
            _right->_v = _v;
            _right->_ans = _f2(_v,_right->_r-_right->_l);
            _v = -1;
        }
        pushdown();
        _ans = _f1(_left->inc_idx(idx, v),_right->inc_idx(idx, v));
        return _ans;
    }

    void pushdown(){
        if(_lazy_tag != 0){
            if(_left){
                if(_left->_v != -1){
                    _left->_v += _lazy_tag;
                    _left->_lazy_tag = 0;
                }
                else{
                    _left->_lazy_tag += _lazy_tag;
                }
                _left->_ans += _f2(_lazy_tag, _left->_r-_left->_l);
            }
            if(_right){
                if(_right->_v != -1){
                    _right->_v += _lazy_tag;
                    _right->_lazy_tag = 0;
                }
                else{
                    _right->_lazy_tag += _lazy_tag;
                }
                _right->_ans += _f2(_lazy_tag, _right->_r-_right->_l);
            }
            _lazy_tag = 0;
        }
    }

    long query(long l, long r){
        /*
        查询线段[right,bottom)的RMQ
        */
        if(l>=r) return 0;
        if(l <= _l && r >= _r)
            return _ans;
        if(_v != -1)
            return _f2(_v, min(_r, r) - max(_l, l));
        long mid = get_mid();
        vector<long> anss;
        if(l < mid)
            anss.emplace_back(_left->query(l, r));
        if(r > mid)
            anss.emplace_back(_right->query(l, r));
        long ans = 0;
        for(int i=0;i<anss.size();i++){
            if(i==0)
                ans = anss[i];
            else
                ans = _f1(ans,anss[i]);
        }
        return ans;
    }
};