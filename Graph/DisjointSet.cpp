#include<vector>

//Disjoint Set
class DisjSet
{
  public:
    std::vector<int> parent;
    std::vector<int> size;

  public:
    DisjSet(int max_size) : parent(std::vector<int>(max_size)),
                            size(std::vector<int>(max_size))
    {
        for (int i = 0; i < max_size; ++i){
            parent[i] = i;
            size[i] = 1;
            }
    }
    int find(int x)
    {
        return x == parent[x] ? x : (parent[x] = find(parent[x]));
    }
    void to_union(int x, int y)
    {
        x = find(x);
        y = find(y);
        if(x==y) return;
        int t;
        if (size[x] < size[y])
        {
            t = x;
            x = y;
            y = t;
        }
        parent[y] = x;
        size[x] += size[y];
    }
    bool is_same(int e1, int e2)
    {
        return find(e1) == find(e2);
    }
};