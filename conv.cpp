#include <bits/stdc++.h>

using namespace std;

string strjoin(vector<char> vc, string sep){
    string ans;
    for(auto &c:vc){
        if(ans.size()){
            ans+=sep;
        }
        ans+=c;
    }
    return ans;
}

string intjoin(vector<int> vi, string sep){
    string ans;
    for(auto &i:vi){
        if(ans.size()){
            ans+=sep;
        }
        ans+=to_string(i);
    }
    return ans;
}

vector<char> strlist(string s){
    vector<char> ans;
    for(auto &c:s)
        ans.push_back(c);
    return ans;
}

vector<string> split(string s, char delim){
    stringstream ss(s);
    string item;
    vector<string> elems;
    while (getline(ss, item, delim)) {
        if (!item.empty()) {
            elems.push_back(item);
        }
    }
    return elems;
}

//[1, 2, 3] => vector<int>{1,2,3}
vector<int> str2vec_i(string s){
    vector<int> ans;
    int a = 0;
    int f = false;
    for(auto c : s){
        if('0'<=c && c<='9'){
            a=a*10+(c-'0');
            f = true;
        }
        else{
            if(f) ans.push_back(a);
            f = false;
            a = 0;
        }
    }
    return ans;
}

//["coffee","donuts","time"] => vector<string>{"coffee","donuts","time"}
vector<string> str2vec_s(string s){
    vector<string> ans;
    string a = "";
    int f = false;
    for(auto c : s){
        if(c!='"' && c!='[' && c!=']' && c!=',' && c!=' '){
            a+=c;
            f = true;
        }
        else{
            if(f) ans.push_back(a);
            f = false;
            a = "";
        }
    }
    return ans;
}

long str2int(string s){
    return stoi(s);
}

string int2str(long i){
    return to_string(i);
}

string float2str(float f){
    return to_string(f);
}

//f(3.1415926,3) => 3.14
string float2str_precision(float f,int prec){
    ostringstream oss;
    oss << setprecision(prec) << f;
    return oss.str();
}

//f(3.1415926,3) => 3.142
string float2str_fixed(float f,int prec){
    ostringstream oss;
    oss << setiosflags(ios::fixed) << setprecision(prec) << f;
    return oss.str();
}

//f(1,3) => 001
string zfill(int i,int n){
    ostringstream oss;
    oss.setf(ios::right);
    oss.fill('0');
    oss.width(n);
    oss << i;
    return oss.str();
}

//f("ab",3) => 0ab
string zfill(string s,int n){
    ostringstream oss;
    oss.setf(ios::right);
    oss.fill('0');
    oss.width(n);
    oss << s;
    return oss.str();
}

float str2float(string s){
    return stof(s);
}

string double2str(double d){
    return to_string(d);
}

double str2double(string s){
    return stod(s);
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