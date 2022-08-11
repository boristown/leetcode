/*
cd primes
g++ primes.cpp
.\a
*/
#include <bits/stdc++.h>

using namespace std;

class Primes{
    public: 
    const static int N = 1e8+10;
    const static int M = 1e7+10;

    public:
    int cnt=0;
    bool isPrime[N];
    int result[M];

    //2倍欧拉筛,找小于N的所有素数
    public:
    void get_primes_o(int n=100000){
        memset(isPrime,1,N*sizeof(bool));
        result[0] = 2;
        int n2 = n / 2;
        cnt = 1;
        int i2 = 0;
        for(int i=3;i<n;i+=2){
            i2++;
            if(isPrime[i2]){
                result[cnt++]=i;
            }
            for(int j=1;j<cnt;j++){
                int e = result[j];
                int ei = e*i;
                if(ei>=n) break;
                isPrime[ei>>1] = 0;
                if(i%e==0) break;
            }
        }
    }
};

int main(){
    int N = 100000000;
    auto a = new Primes();
    a->get_primes_o(N);
    cout<<a->cnt<<endl;
    for(int i = 0;i<10;i++){
        cout<<a->result[i]<<endl;
    }
    return 0;
}