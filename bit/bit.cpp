// 位运算
// https://oi-wiki.org/math/bit/
#include<string>
#include <bitset>
#include<stack>

using namespace std;

//获取一个二进制长度为n且全是1的数字
int allone(int n) { return (1<<n)-1; }

//判断一个数是不是2的非负整数次幂
bool isPowerOfTwo(int n) { return n > 0 && (n & (n - 1)) == 0; }

//对2的非负整数次幂取模：
int modPowerOfTwo(int x, int mod) { return x & (mod - 1); }

//获取一个数二进制的某一位：
//获取 a 的第 b 位，最低位编号为 0
int getBit(int a, int b) { return (a >> b) & 1; }

// 将一个数二进制的某一位设置为0：
// 将 a 的第 b 位设置为 0 ，最低位编号为 0
int unsetBit(int a, int b) { return a & ~(1 << b); }

// 将一个数二进制的某一位设置为1：
// 将 a 的第 b 位设置为 1 ，最低位编号为 0
int setBit(int a, int b) { return a | (1 << b); }

// 将一个数二进制的某一位取反：
// 将 a 的第 b 位取反 ，最低位编号为 0
int flapBit(int a, int b) { return a ^ (1 << b); }

// 求 x 的汉明权重
int popcount(int x) {
    int cnt = 0;
    while (x) {
        cnt += x & 1;
        x >>= 1;
    }
    return cnt;
}

string Dec2Binary(long n)
{
    bitset<16> bint{n};
    return bint.to_string();
}

long Binary2Dec(string s){
    bitset<16> bint{s};
    return bint.to_ulong();
}

//任意进制转十进制
long any2dec(string origin, int x){
    long ans=0;
    int i=0;
    while(origin.size()!=i)
    {
        ans*=x;             //我这里是把1看成0，把0看成1来算的。这样比较方便。其实都一样。
        ans+=origin[i]-'0';
        i++;
    }
    return ans;
}

string dec2any(int n,int r){
    string ans;
    stack<int> s;
    while(n)
    {
        s.push(n%r);
        n/=r;
    }
    while(!s.empty())
    {
        switch(s.top())
        {
            case 10:ans+='A';break;
            case 11:ans+='B';break;
            case 12:ans+='C';break;
            case 13:ans+='D';break;
            case 14:ans+='E';break;
            case 15:ans+='F';break;//这些都是为了能转化为十六进制。
            default:ans+=s.top();break;
        }
        s.pop();
    }
    return ans;
}