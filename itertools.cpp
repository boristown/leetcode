#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> permutations(vector<int> vi) {
  vector<vector<int>> ans;
  sort(vi.begin(),vi.end());
  do{
    ans.push_back(vector<int>(vi));
  }
  while (next_permutation(vi.begin(), vi.end()));
}

template <typename T>
void combine_inner(T &data, int start, int n, int m, int depth, T temp,vector<T> &result)
{
    if (depth == m - 1)
    {
        //最内层循环 将temp加入result
        for (int i = start; i < n - (m - depth - 1); ++i)
        {
            temp[depth] = data[i];
            result.push_back(temp);
        }
    }
    else
        for (int i = start; i < n - (m - depth - 1);++i)
    {
        temp[depth] = data[i];//每层输出一个元素
        combine_inner(data,i + 1, n, m, depth+1,temp,result);
    }
}

//T可以调入vector<int>, string等，需要支持下标[]操作及size()函数
//example     
//string s("ABCDEF");
//vector<string> result = combine(s, 3);
template <typename T>
vector<T> combine(T &data,int m)
{
    if (m <= 0)
        return{};
    int depth = 0;
    vector<T> result;
    T temp(m,0);
    combine_inner(data,0, data.size(), m, depth,temp,result);
    return result;
}