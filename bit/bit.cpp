// 位运算
// https://oi-wiki.org/math/bit/
#include<string>
#include <bitset>

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
    return int(str(origin), base = x) // origin必须是字符串
}

def dec2any(n,x):
    '''
    10进制转N进制
    n为待转换的十进制数，x为机制，取值为2-16
    适用场景：进制转换
    '''
    a=['0','1','2','3','4','5','6','7','8','9','A','b','C','D','E','F']
    b=[]
    while True:
        s=n//x  # 商
        y=n%x  # 余数
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    x=""
    for i in b:
        x+=a[i]
    return x